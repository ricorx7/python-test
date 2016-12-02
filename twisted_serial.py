from twisted.internet import protocol, reactor
from twisted.internet.serialport import SerialPort
from twisted.protocols import basic

class DeviceADCP(basic.LineReceiver):

    def connectionMade(self):
        print('Connection made!')
        #self.sendString('CSHOW\n')

    def connectionLost(self, reason):
        self.factory.clients.remove(self)
        print('Connection lost')

    def dataReceived(self, data):
        print("Response: {0}", format(data))


SerialPort(DeviceADCP(), '/dev/cu.usbserial-FTYNODPO', reactor, baudrate=115200)
reactor.run()


