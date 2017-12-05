from BluetoothManager import BluetoothManager

class BluetoothManagerMock(BluetoothManager):
    def __init__(self):
        self.startServer()

    def startServer(self):
        print("Starting BT server")


    def connect(self):
        self.data = "41.703054 -86.239018" #Hardcode the coordinates here.
        self.hasData = True
