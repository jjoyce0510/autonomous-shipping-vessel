# Class that will handle establishing a BT connection and receiving the data
from bluetooth import *

class BluetoothManager:

    hasData = False
    data = ""

    def __init__(self):
        # Create the server
        self.serverSock = BluetoothSocket(RFCOMM)
        self.serverSock.bind(("", PORT_ANY))
        self.serverSock.listen(1)
        self.port = self.serverSock.getsockname()[1]
        self.uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
        self.startServer()

    def startServer(self):
        advertise_service(self.serverSock, "SampleServer", service_id = self.uuid,
                          service_classes = [ self.uuid, SERIAL_PORT_CLASS ], profiles = [ SERIAL_PORT_PROFILE ])
        print("Waiting for connection on RFCOMM channel %d" % self.port)

        self.waitForConnection()

    def connect(self):
        while not self.hasData:
            clientSock, clientInfo = self.serverSock.accept()
            print("Accepted connection from ", clientInfo)
            try:
                while True:
                    newData = clientSock.recv(1024)
                    self.data = self.data + newData
                    if len(newData) == 0: break
                    else: self.hasData = True

            except IOError:
                pass

            print("Disconnected.")
            clientSock.close()


    def getData(self):
        return self.data

    def hasData(self):
        return self.hasData()