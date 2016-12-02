'''Connect through TCP to receive serial data.  This will
allow multiple TCP connections to one serial port.'''

from twisted.internet import reactor, protocol, endpoints
from twisted.protocols import basic
from twisted.internet.serialport import SerialPort

class SerialDevice(basic.LineReceiver):
    '''Serial device that will send data to all the TCP clients connected'''
    def __init__(self, factory, tcp_server):
        self.factory = factory
        self.tcp_server = tcp_server

    def connectionMade(self):
        '''Connect the serial port'''
        print('Connection made!')
        #self.sendString('CSHOW\n')

    def connectionLost(self, reason):
        '''Disconnect the serial port'''
        #self.factory.clients.remove(self)
        print('Connection lost')

    def dataReceived(self, data):
        '''Send data to all the clients connected on the TCP port'''
        #print("Response: {0}", format(data))
        for c in self.tcp_server.factory.clients:
            c.transport.write(data)
            #c.sendLine(data)

    def lineReceived(self, data):
        '''Do nothing for now'''
        pass

    def rawDataReceived(self, data):
        '''Do nothing for now'''
        pass


class SerialTcpProtocol(basic.LineReceiver):
    '''Create TCP Connections for user that want to get serial data'''
    delimiter = ""

    def __init__(self, factory, commport, baud):
        self.factory = factory

        # Create a Serial Port device to read in serial data
        SerialPort(SerialDevice(self, self), commport, reactor, baudrate=baud)
        print('Serial Port Thread started')


    def connectionMade(self):
        '''Add TCP connections'''
        self.factory.clients.add(self)
        print('Connection made')

    def connectionLost(self, reason):
        '''Disconnect TCP Connections'''
        self.factory.clients.remove(self)
        print('Connection lost')

    def lineReceived(self, line):
        pass
        #for c in self.factory.clients:
            #source = u"<{}> ".format(self.transport.getHost()).encode("ascii")
            #c.sendLine(source + line)
            #print('line received: ', line)

    def rawDataReceived(self, data):
        pass
    #    for c in self.factory.clients:
            #source = u"<{}> ".format(self.transport.getHost()).encode("ascii")
            #c.sendLine(source + data)
   #         print('data received: ', data)


class PubFactory(protocol.Factory):
    '''Create a serial connection and allow TCP clients to view the data'''
    def __init__(self):
        self.clients = set()

    def buildProtocol(self, addr):
        return SerialTcpProtocol(self, '/dev/cu.usbserial-FTYNODPO', 115200)

# Set the PORT to output ADCP data
endpoints.serverFromString(reactor, "tcp:55056").listen(PubFactory())
reactor.run()
