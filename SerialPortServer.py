"""Send data from serial port to all TCP/IP connections"""

import os
import socketserver
import sys
import threading
import serial

class SerialPortServerRequestHandler(socketserver.BaseRequestHandler):
    """Handle a user connecting to the TCP/IP Port"""
    def handle(self):
        # Echo the back to the client
        #data = self.request.recv(1024)
        #cur_pid = os.getpid()
        #response = '%s: %s' % (cur_pid, data)
        #self.request.send(response.encode())
        print('Client address connection:', self.client_address)
        print('Server: ', self.server)
        self.server.conn_dict[self.client_address[0]] = self.request
        return
    def finish(self):
        """Called when handler is completed"""
        #Remove self from dictionary
        del self.server.conn_dict[self.client_address[0]]


class ForkingServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    """Create a Forking TCP/IP Server.  A thread is created for every connection"""
    pass

class SerialPortServer:
    """Connect to a serial port.  Then allow user to receive data from
        the serial port based off every TCP/IP connection"""

    def __init__(self, commport, baud):
        #Create a dictonary to hold all connections
        self.conn_dict = {}

        # Connect to serial port first
        # Give the list of serial ports python -m serial.tools.list_ports -v
        try:
            self.serial_port = serial.Serial(commport, baud)
            self.is_alive = False
        except serial.SerialException as err:
            print("Serialport Failed to connect", err)
            sys.exit()
        except:
            print("Serialport Failed to connect")
            sys.exit()

        # Create a TCP server that forks all incoming connections
        # so that they run on a seperate thread.
        self.server = socketserver.ForkingTCPServer(
            ("0.0.0.0", 55056),
            RequestHandlerClass=SerialPortServerRequestHandler,
            bind_and_activate=False)
        self.server.allow_reuse_address = True
        self.server.server_bind()
        self.server.server_activate()
        print('Socket server created: ', self.server.server_address)

        # Create a thread to run the forking TCP server
        self.thread_tcp_server = threading.Thread(target=self.server.serve_forever)
        self.thread_tcp_server.setDaemon(True) # don't hang on exit
        self.thread_tcp_server.name = 'tcp server'
        self.thread_tcp_server.start()
        print('Server loop running in process:', os.getpid())

        # Create a thread to read the serial data
        self.thread_serialport_read = threading.Thread(target=self.broadcast_serial_data)
        self.thread_serialport_read.daemon = True
        self.thread_serialport_read.name = 'serial->socket'

        # Start Serial Port Reading
        self.is_alive = True
        self.thread_serialport_read.start()
        print('Serial Port Thread started')

    def close(self):
        """Close the server."""
        self.server.socket.close()
        self.is_alive = False
        self.serial_port.close()
        self.thread_serialport_read.join()

    #def broadcast(self, port):
        #"""Setup broadcasting the Serial data over UDP"""
        #timeout = 60.0 # Sixty seconds
        #l = task.LoopingCall(self.broadcast_serial_data(port))
        #l.start(timeout) # call every sixty seconds
        #self.is_alive = True
        #print("Broadcast Serial Data Started on Port: " + str(port))
        #self.broadcast_serial_data(port)
        #self.thread_serialport_read.start()


    def broadcast_serial_data(self):
        """Broadcast the serial data to the UDP port"""
        while self.is_alive:
            try:
                data = self.serial_port.read(self.serial_port.in_waiting)
                if not data:
                    break
                for key in self.conn_dict.items():
                    self.conn_dict[key].request.send(data)
            except SystemExit:
                raise



if __name__ == '__main__':
    #import socket
    #import threading

    # Create the server
    SERVER = SerialPortServer('/dev/cu.usbserial-FTYNODPO', 115200)

    #ip, port = SERVER.server.server_address # find out what port we were given


    # Connect to the server
    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.connect((ip, port))

    # Send the data
    #message = 'Hello, world'
    #print('Sending : "%s"' % message)
    #len_sent = s.send(message.encode())

    # Receive a response
    #response = s.recv(1024)
    #print('Received: "%s"' % response)

    while True:
        n = input("Press any key to stop")
        if n != '9':
            break

    # Clean up
    #s.close()
    SERVER.close()
