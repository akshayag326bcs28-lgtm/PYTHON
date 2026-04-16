class Fan:
    def __init__(self, speed="Medium"):
        self.speed = speed

    def status(self):
        print("The fan is running at ",self.speed," speed.")
my_fan = Fan()
my_fan.status()
