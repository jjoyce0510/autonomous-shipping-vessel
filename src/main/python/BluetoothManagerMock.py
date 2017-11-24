from BluetoothManager import BluetoothManager

class BluetoothManagerMock(BluetoothManager):
    def __init__(self):
        self.startServer()

    def startServer(self):
        print("Starting BT server")


    def connect(self):
        self.data = "40.0 -79.0" #Hardcode the coordinates here.
        self.hasData = True
