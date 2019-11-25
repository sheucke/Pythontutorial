class Vehicle:
    def start(self):
        print("started...")

    def stop(self):
        print("Stopped...")


class Car(Vehicle):
    def Result(self):
        super().start()
        super().stop()


c = Car()
c.Result()
