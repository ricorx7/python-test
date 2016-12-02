# python-test
Expermenting with Python

__To Compile pyside2 from source for OSX__

##Download and install QT5.6
```
curl -O https://raw.githubusercontent.com/Homebrew/homebrew-core/fdfc724dd532345f5c6cdf47dc43e99654e6a5fd/Formula/qt5.rb
```
```
brew install ./qt5.rb
```
##Download pyside2
```
git clone --recursive http://code.qt.io/cgit/pyside/pyside-setup.git/
```

##Install pyside3 with python3 and QT5.6
```
python3 setup.py install ---ignore-git --build-tests --qmake=/usr/local/Cellar/qt5/5.6.1-1/bin/qmake --cmake=/usr/local/bin/cmake --openssl=/usr/bin/openssl
```


__twisted_SerialPortServer.py__
This will allow a user to connect through TCP to a serial port connection.  It allows mulitple users to connect and receive the same serial data.


__SerialPortServer__
This will allow the creation of multiple TCP connections and pass the serial data to all connections 

