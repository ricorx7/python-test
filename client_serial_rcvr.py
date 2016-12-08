

import socket
import sys, getopt

class tcp_reader_client():
    """
    Create a TCP reader class
    """
    def __init__(self, port):
        self.port = port
        self.socket = None
        self.reconnect(port)
        self.read()

    def reconnect(self, port):
        """
        Connect to the server.
        """
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect(('localhost', port))
        except ConnectionRefusedError as err:
            print(err)
            sys.exit(2)
        except:
            print('Error Opening socket')
            sys.exit(2)

    def read(self):
        """
        Read data from the serial port
        """
        try:
            while True:
                # Receive a response
                response = self.socket.recv(1024)
                print('"%s"' % response)

                if len(response) == 0:
                    print("Disconnected")

                    # Close the socket
                    self.close()

                    # Reconnect to the server
                    self.reconnect(self.port)

                    # Try to read again
                    self.read()

        except KeyboardInterrupt:
            # Ctrl-C will stop the application
            pass
        except:
            pass

    def close(self):
        """
        Close the socket.
        """
        self.socket.close()

if __name__ == '__main__':
    argv = sys.argv[1:]
    port = 55056
    try:
        opts, args = getopt.getopt(argv,"p:",["port="])
    except getopt.GetoptError:
        print('client_serial_rcvr.py  -p <port>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('client_serial_rcvr.py -p <port>')
            sys.exit()
        elif opt in ("-p", "--port"):
            port = int(arg)

    # Read from TCP port
    reader = tcp_reader_client(port)
    reader.close()
    print("Socket Closed")

""""
    # Connect to the server
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', port))
    except ConnectionRefusedError as err:
        print(err)
        sys.exit(2)
    except:
        print('Error Opening socket')
        sys.exit(2)

    try:
        while True:
            # Receive a response
            response = s.recv(1024)
            print('"%s"' % response)

            if len(response) == 0:
                print("Disconnected")
                # Connect to the server
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect(('localhost', port))
                except ConnectionRefusedError as err:
                    print(err)
                    sys.exit(2)
                except:
                    print('Error Opening socket')
                    sys.exit(2)
    except KeyboardInterrupt:
        # Ctrl-C will stop the application
        pass
    except:
        pass

    s.close()
"""


