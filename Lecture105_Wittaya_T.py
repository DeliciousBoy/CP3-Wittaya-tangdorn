class Vehicle:
    lecenseCode = ""
    serialCode = ""
    def turnonAirconditioner(self):
        print("Turn on: Air")

class Car(Vehicle):
    pass

class Pickup(Vehicle):
    pass

class Van(Vehicle):
    pass

class Estatecar(Vehicle):
    pass

car = Car()
pickup = Pickup()
van = Van()
estatecar = Estatecar()

car.turnonAirconditioner()
pickup.turnonAirconditioner()
van.turnonAirconditioner()
estatecar.turnonAirconditioner()
