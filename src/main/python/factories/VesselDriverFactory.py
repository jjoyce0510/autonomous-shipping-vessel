from src.main.python.control.driver.VesselDriver import VesselDriver
from ObjectDetectorFactory import ObjectDetectorFactory
from VesselControlsFactory import VesselControlsFactory
from SingletonFactory import SingletonFactory


class VesselDriverFactory(SingletonFactory):
    def getInstance(self):
        return VesselDriver(ObjectDetectorFactory().createInstance(), VesselControlsFactory().createInstance())
