class CarFactory:

    def create_car(self,brand):
        if brand == "Benz":
            return Benz()
        elif brand == "BMW":
            return BMW()
        elif brand == "BYD":
            return BYD()
        else:
            return "None"


class Benz:
    pass

class BMW:
    pass

class BYD:
    pass

factory = CarFactory()
c1 = factory.create_car("Benz")
c2 = factory.create_car("BMW")
print(c1.__class__)
print(c2)