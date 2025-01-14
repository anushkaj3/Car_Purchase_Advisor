import math


class Car:
    """
    A class to store the Car details

    ---Attributes--
    car_code : str
            a string to store the car code
    car_name : str
            a string to store the name of the car
    car_capacity : int
            an integer to store the capacity of the car
    car_horsepower: float
            a float to store the horsepower of the car
    car_weight:float
            a float to store the car weight
    car_types : string
            a string to store the car types - AWD , RWD or FWD

    ---Methods---
    probationary_licence_prohibited_vehicle():
        Returns True / False if the car is prohibited based on a probationary licence
    found_matching_car():
        Returns True if the car_code taken as input matches the car code of the object
    get_car_type():
        Returns the car type corresponding to the current car instance

"""

    def __init__(self, car_code="", car_name="", car_capacity=2, car_horsepower=0.0, car_weight=0.0, car_type=""):
        #Save values for the current instance of the Car class
            self.car_code = car_code
            self.car_name = car_name
            self.car_capacity = car_capacity
            self.car_horsepower = car_horsepower
            self.car_weight = car_weight
            self.car_type = car_type

    def __str__(self):
        formatted_str = self.car_code+", "+self.car_name+", "+str(self.car_capacity)+", "+str(self.car_horsepower)+", "
        formatted_str += str(self.car_weight)+", "+self.car_type
        return formatted_str

    def probationary_licence_prohibited_vehicle(self):
        # Calculate the power to mass ratio
        power_to_mass = (self.car_horsepower/ self.car_weight)
        # round up the power to mass ratio to check if it is greater than 130 , the car is restricted for probationary licence
        if (math.ceil((power_to_mass * 1000)) > 130 ):
            return True
        return False

    def found_matching_car(self,car_code):
        # Check if the car code of the instance matches the car code sent as an argument
        if self.car_code == car_code:
            return True
        return False

    def get_car_type(self):
        # Returns the Car type of the instance of the car.
        return self.car_type

