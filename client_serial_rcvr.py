import socket

if __name__ == '__main__':
    #import socket
    #import threading

    # Create the server
    #SERVER = SerialPortServer('/dev/cu.usbserial-FTYNODPO', 115200)

    #ip, port = SERVER.server.server_address # find out what port we were given


    # Connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 55056))

    # Send the data
    #message = 'Hello, world'
    #print('Sending : "%s"' % message)
    #len_sent = s.send(message.encode())
    count = 0

    while count < 1000:
        count += 1
        # Receive a response
        response = s.recv(1024)
        print('"%s"' % response)

    s.close()

