import random
import string
from car import Car

class Order:
    """
    Order class generates the unique order ID
    ---Attributes---
    order_car : object
        the object of car class
    order_retailer : object
        the object of retailer class
    order_creation_time : int
        integer of the current time
    order_id : str
        string of the order id generated
    ---Methods---
    generate_order_id ():
        Generates the order id
    """
    def __init__(self,order_id ="" ,order_car ="",order_retailer="",order_creation_time=""):

        self.order_car = order_car
        self.order_retailer = order_retailer
        self.order_creation_time = order_creation_time
        self.order_id = self.generate_order_id(order_car.car_code)

    def __str__(self):
        formatted_str = str(self.order_id)+ ", " + self.order_car.car_code + ", " + str(self.order_retailer.retailer_id)+", "+ str(self.order_creation_time)
        return formatted_str

    def generate_order_id(self,car_code):
        length = 6
        str_1 = "~!@#$%^&*"
        length_str_1 = len(str_1)
        new_str = ""
        # choose a random lowercase character
        generated_str = ''.join(random.choices(string.ascii_lowercase, k=length))
        for i in range(0, len(generated_str)):
            # the second, fourth and 6th character are set to upper case
            if i % 2 != 0:
                abc = generated_str[i].upper()
                new_str += abc
            else:
                new_str += generated_str[i]
        for i in range(0, len(new_str)):
            # find the ASCII code of the letter
            numeric = ord(new_str[i])
            # raise the ascii code to the power of 2 and divide by length of str_1
            numeric = (numeric ** 2) % length_str_1
            corres_char = str_1[numeric]
            if i != 0:
                new_str += corres_char * i
        unique_id = new_str + car_code + str(self.order_creation_time)
        return unique_id









