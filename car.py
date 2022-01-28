class Car(object):

    """
    Represent a car in  my virtual world.

    Arguments:
    make (string): car make.
    model (string): car model.
    fuel_efficiency (float): in miles per gallon.
    mileage (float, optional): current mileage on car in miles, defaults to 0.
    gas (float, optional): current gas in the tank in gallons, defaults to 0.

    Attributes:
    make (string): car make.
    model (string): car model.
    fuel_efficiency (float): in miles per gallon.
    mileage (float): current mileage on the car in miles.
    gas_in_tank (float): current gas in the tank in gallons.
    """

    def __init__(self,  make,  model, fuel_efficiency, mileage=0, gas=0):
        self.make = make
        self.model = model
        self.fuel_efficiency = fuel_efficiency
        self.mileage = mileage
        self.gas_in_tank = gas

    def add_gas(self, amount):
        """
        Add gas to the car.
        Parameter:
        amount (float): the amount of gas to be added in gallons.
        Return:
        the updated car object (Car).
        """
        self.gas_in_tank += amount
        return self

    def drive(self, distance):
        """
        Drive a car a given distance, if possible.
        If there is not enough gas, drive as much as possible.
        Parameter:
        distance (float):  the distance to be driven in miles.
        Return:
        the updated car object (Car)
        """
        max_distance = self.fuel_efficiency * self.gas_in_tank
        if distance <= max_distance:  # we can drive the distance
            self.mileage += distance
            self.gas_in_tank = (self.gas_in_tank -
                                distance / self.fuel_efficiency)
        else:   # not enough gas
            self.mileage += max_distance  # drive as far as possible
            self.gas_in_tank = 0
        return self
