
# Only hold one instance of this for inner class to be a singleton.
class SingletonFactory:
    instance = None

    def createInstance(self):
        if self.instance is None:
            self.instance = self.getInstance()
        return self.instance

    def getInstance(self):
        return None