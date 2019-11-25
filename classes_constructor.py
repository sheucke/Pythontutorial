class Car:
    def __init__(self, model, color, speed):
        self.model = model
        self.color = color
        self.speed = speed

    def start(self):
        print(self.model + " is started")

    def stop(self):
        print(self.model + " stoped")

    def accelerate(self):
        print(self.model + " is accelerating")


suzuki_car = Car("suzuki", "red", 80)
ferrari_car = Car("ferrari", "black", 40)

suzuki_car.start()
ferrari_car.start()
ferrari_car.stop()
suzuki_car.accelerate()
