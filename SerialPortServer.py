import os
import socketserver

class SerialPortServerRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # Echo the back to the client
        data = self.request.recv(1024)
        cur_pid = os.getpid()
        response = '%s: %s' % (cur_pid, data)
        self.request.send(response.encode())
        return

class SerialPortServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

if __name__ == '__main__':
    import socket
    import threading

    address = ('localhost', 0) # let the kernel give us a port
    #server = ForkingEchoServer(address, ForkingEchoRequestHandler)
    server = socketserver.ForkingTCPServer(
        ("0.0.0.0", 8080),
        RequestHandlerClass=SerialPortServerRequestHandler,
        bind_and_activate=False)

    server.allow_reuse_address = True
    server.server_bind()
    server.server_activate()

    ip, port = server.server_address # find out what port we were given

    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True) # don't hang on exit
    t.start()
    print('Server loop running in process:', os.getpid())

    # Connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    # Send the data
    message = 'Hello, world'
    print('Sending : "%s"' % message)
    len_sent = s.send(message.encode())

    # Receive a response
    response = s.recv(1024)
    print('Received: "%s"' % response)

    # Clean up
    s.close()
    server.socket.close()