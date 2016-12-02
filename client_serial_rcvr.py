import socket
import sys, getopt

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
    except KeyboardInterrupt:
        # Ctrl-C will stop the application
        pass

    s.close()
    print("Close the socket")

