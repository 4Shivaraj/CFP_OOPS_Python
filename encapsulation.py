"""
ENCAPSULATION:
it is another way of extending class, that consist wrapping/binding of objects by hiding the implementation.
in case of inheritance,variable and function inside the parent class that can be re-utilised,
even in case of encapsulation we will be able to re-utilise, but in little different way,
when we get a requirement that we need go create a classes and create It's variable but not show you actual
implementation,when you do the inheritance unless until your not aware about parent class and its variable,
functions and object you will not be able to use it,because we will inherit and try to call variable function
inside parent class,
but in case encapsulation, we have to call something from parent, let suppose in parent if we did some method or
function implementation if I don't want to expose that implementation to you,but still you have to re-utilise it.

Example: capsules composition of capsules is hidden
"""
from oops_log import get_logger

lg = get_logger(name="(Encapsulation)", file_name="oops_log.log")


class Tyres:
    def __init__(self, branch, belted_bias, opt_pressure):
        self.branch = branch
        self.belted_bias = belted_bias
        self.opt_pressure = opt_pressure

    def __str__(self):
        return ("Tyres: \n \tBranch: " + self.branch +
                "\n \tBelted-bias: " + str(self.belted_bias) +
                "\n \tOptimal pressure: " + str(self.opt_pressure))


class Engine:
    def __init__(self, fuel_type, noise_level):
        self.fuel_type = fuel_type
        self.noise_level = noise_level

    def __str__(self):
        return ("Engine: \n \tFuel type: " + self.fuel_type +
                "\n \tNoise level: " + str(self.noise_level))


class Body:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return "Body: \n \tSize: " + self.size


class Car:
    def __init__(self, name, tyres, engine, body):
        self.name = name
        self.tyres = tyres
        self.engine = engine
        self.body = body

    def __str__(self):
        return str(self.tyres) + "\n" + str(self.engine) + "\n" + str(self.body) + " " + str(self.name)


if __name__ == '__main__':
    tire_obj = Tyres("Pirelli", True, 2.0)
    engine_obj = Engine("Diesel", 3)
    body_obj = Body("Medium")
    car_obj = Car("toyota", tire_obj, engine_obj, body_obj)
    lg.debug(car_obj)

"""
Tyres: 
 	Branch: Pirelli
 	Belted-bias: True
 	Optimal pressure: 2.0
Engine: 
 	Fuel type: Diesel
 	Noise level: 3
Body: 
 	Size: Medium toyota
"""
