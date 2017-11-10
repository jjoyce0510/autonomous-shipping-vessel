
class SingletonFactory:
    instance = None

    def getInstance(self):
        if self.instance is None:
            self.instance = self.createInstance()
        return self.instance

    def createInstance(self):
        return None