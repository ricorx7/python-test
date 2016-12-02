import logging
from twisted.protocols.basic import LineReceiver
from twisted.protocols.basic import LineReceiver

from twisted.internet import reactor
from twisted.internet.serialport import SerialPort
from twisted.python import usage
import threading

class THOptions(usage.Options):
    optParameters = [
        ['baudrate', 'b', 115200, 'Serial baudrate'],
        ['port', 'p', '/dev/cu.usbserial-FTYNODPO', 'Serial port to use'],]


class Echo(LineReceiver):
    def processData(self, data):
        print(data)

    def lineReceived(self, line):
        try:
            data = line.rstrip()
            #logging.debug(data)
            self.processData(data)
            #print(line.rstrip())
            #pass
        except ValueError:
            logging.error('Unable to parse data %s' % line)
            return

def SerialInit():
    o = THOptions()
    try:
        o.parseOptions()
    except(usage.UsageError, errortext):
        logging.error('%s %s' % (sys.argv[0], errortext))
        logging.info('Try %s --help for usage details' % sys.argv[0])
        raise(SystemExit, 1)

    baudrate = o.opts['baudrate'] #int('115200')
    port = o.opts['port']
    logging.debug('About to open port %s' % port)
    s = SerialPort(Echo(), port, reactor, baudrate=baudrate)
    reactor.run()


#thread.start_new_thread(SerialInit())


if __name__ == '__main__':
    print("-----")
    #s.write('123456789')
    #s.write("\n")
    SerialInit()
