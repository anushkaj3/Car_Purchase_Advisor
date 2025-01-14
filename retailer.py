import random


class Retailer:
    """
    The Retailer class stores information of the retailer, and generates a unique retailer
    for every retailer instance.

    ---Attributes---
    retailer_id : int
        an integer that stores a retailer id of 8 digits
    retailer_name : str
        a string that stores the retailer name

    ---Methods---
    generate_retailer_id():
        generates unique retailer id
    """

    def __init__(self,retailer_id,retailer_name=""):
        # save values of the instance
        self.retailer_id = retailer_id
        self.retailer_name = retailer_name

    def __str__(self):
        formatted_str = str(self.retailer_id)+","+self.retailer_name
        return formatted_str

    def generate_retailer_id(self,list_retailer):
        # Generate a random 8 digit integer
        new_retailer_id = (random.randint(10000000, 99999999))
        # Check if the generated number already exists as a retailer id
        existing_retailer_id = [item.retailer_id for item in list_retailer]
        while True:  # keep checking until find the unique one
            if new_retailer_id in existing_retailer_id:
                new_retailer_id = random.randint(10000000, 99999999)
            else:
                break
        # assign the generated unqiue id to the retailer id .
        self.retailer_id = new_retailer_id
