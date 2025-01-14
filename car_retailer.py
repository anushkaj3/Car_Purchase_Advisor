from retailer import Retailer
from order import Order
from car import Car
import re
import random
import time
import os


class CarRetailer(Retailer):
    """
    CarRetailer class manages majority of the functions for a car advisory system

    ---Attributes---
    car_stock_list : list
        A list of car objects
    carretailer_address : str
         A string of the car retailer address
    carretailer_business_hours : tuple of float
        A tupple of floats that contain the start time and end time that the car retailer runs for
    carretailer_stock : list of str
        A list of strings holding the car codes

    ---Methods---
    load_current_stock():
        Loads the current stock of cars as per the stock.txt file
    is_operating():
        Checks if the car retailer is currently operating
    get_all_stock():
        Returns a list of Car class objects for the current retailer_id
    get_postcode_distance():
        Returns the difference between the postcode that the user enters and the post code of the retailer
    remove_from_stock():
        Returns True if  car is removed from the stock file and the current car stock has been updated
    add_to_stock():
        Returns True if a car is successfully added to the stock file
    get_stock_by_car_type():
        Returns a list of Car class objects that matches the car type sent as an input
    get_stock_by_licence_type():
        Returns a list of Car class objects of cars that are not forbidden by licence
    car_recommendation():
        Returns a randomly select car object from the car stock
    create_order():
        Creates an order for the retailer id and car code as requested by the user

    """
    car_stock_list = []

    def __init__(self, retailer_id, retailer_name, carretailer_address="",
                 carretailer_business_hours=(0.0,0.0), carretailer_stock=[]):
            # store values for the instnace of CarRetailer
            super().__init__(retailer_id,retailer_name)
            self.carretailer_address = carretailer_address
            self.carretailer_business_hours = carretailer_business_hours
            self.carretailer_stock = carretailer_stock

    def __str__(self):
        formatted_str = super().__str__()+","+str(self.carretailer_address)+","
        formatted_str += str(self.carretailer_business_hours[0])+str(self.carretailer_business_hours[1])+","
        for car in self.carretailer_stock:
            formatted_str += car +","
        return formatted_str

    def load_current_stock(self,path):
        lines = ""
        # open the file which stores the stock information in read mode
        input_handle_retailer = open(path, 'r')
        # read each line of the file
        for line in input_handle_retailer:
            line_tokens = line.split(",")
            # check if the line corresponds to the current retailer instance
            if line_tokens[0] == self.retailer_id:
                lines = "".join([line.strip()])
        if lines != "" :
            # extract data rom the stock file and find the car codes
            pattern = r"\[(.*?)\]"
            extracted_data = re.findall(pattern, lines)
            pattern1 = r"'(.*?)'"
            data = re.findall( pattern1 ,extracted_data[0])
            # appends the car codes from the stock file in the carretailer_stock
            for each in data:

                self.carretailer_stock.append(each[0:8])
        input_handle_retailer.close()

    def is_operating(self,cur_hour):
        # check if the current time is within the retailers business hours
        if (cur_hour >= self.carretailer_business_hours[0]) and (cur_hour <= self.carretailer_business_hours[1]):
            return True
        return False

    def get_all_stock(self):
        # gets all stock of the car objects for the rtailer instance
        cars_current = []

        for each in CarRetailer.car_stock_list:

            if each.car_code in self.carretailer_stock:

                cars_current.append(each)
        return cars_current

    def get_postcode_distance(self,postcode):
        # extract the postcode from the carretailer_address
        extrcar_act = re.findall(r" [0-9]{4}",self.carretailer_address)
        # calculate the absolute difference
        postcode_diff = abs(int(extrcar_act[0]) - int(postcode))
        return postcode_diff

    def remove_from_stock(self,car_code):
        str_line = ""
        lines = ""
        for i in range(0, len(self.carretailer_stock)):
            # check if the car exists in the current carretailer_stock
            if self.carretailer_stock[i] == car_code:
                obj = self.carretailer_stock[i]
                self.carretailer_stock.remove(obj)
                # open stock folder in read mode
                input_handle_retailer = open('stock.txt', 'r')
                for line in input_handle_retailer:
                    line_tokens = line.split(",")
                    # check if the line in the txt file corresponds to the current retailer id
                    if line_tokens[0] == str(self.retailer_id):
                        lines = "".join([line.strip()])
                if lines != "":
                    input_handle_retailer.close()
                    # extract data from the txt file
                    pattern = r'\[(.*?)\]'
                    extracted_data = re.findall(pattern,lines)
                    pattern1 = r"'(.*?)'"
                    ex_data = re.findall(pattern1 , extracted_data[0])
                    # remove the car code from the txt file
                    for each in ex_data:
                        if each[0:8] == str(obj):
                            data = each
                            ex_data.remove(data)
                    for i in range(0,len(ex_data)):
                        if i == 0:
                            str_line += "'"+ex_data[i]+"'"
                        else:
                            str_line += ", '" + ex_data[i] + "'"
                    input_handle_retailer = open('stock.txt', 'r')
                    file_data = input_handle_retailer.read()
                    input_handle_retailer.close()
                    # replace the text in the file with the new update car stock
                    file_data = file_data.replace(extracted_data[0], str_line)
                    output = open('stock.txt', "w")
                    output.write(file_data)
                    output.close()
                return True
        return False

    def add_to_stock(self,car):
        lines = ""
        # check if car code is already present with the retailer id
        if car.car_code in self.carretailer_stock:
            return False
        else:
            self.carretailer_stock.append(car.car_code)
            CarRetailer.car_stock_list.append(car)
            # check if the stock file exists
            check = os.path.isfile('stock.txt')
            if check is not True :
                # if the stock file is not present open the file in append mode
                output = open('stock.txt', 'a')
                # save the retailer information and the car stock
                pattern1 = r"([A-Z]{3}) ([0-9]{4})"
                pattern2 = r"\1\2"
                address = re.sub(pattern1,pattern2, self.carretailer_address)
                lines = str(self.retailer_id)+","+" "+self.retailer_name+","+" "+str(address)+","
                lines += " "+str(self.carretailer_business_hours)+","+" "+"['"+str(car)+"']"
                # write the stock details to the stock.txt file
                output.writelines(lines)
                output.write('\n')
                output.close()
            # if the stock file exists then open the file in read mode to check if the retailer record exists
            else:
                input = open('stock.txt', 'r')

                for line in input:
                    line_tokens = line.split(",")
                    if line_tokens[0] == str(self.retailer_id):
                        lines = "".join([line.strip()])

                if lines == "":
                    output = open('stock.txt', 'a')
                    pattern1 = r"([A-Z]{3}) ([0-9]{4})"
                    pattern2 = r"\1\2"
                    address = re.sub(pattern1, pattern2, self.carretailer_address)
                    lines = str(self.retailer_id) + "," + " " + self.retailer_name + "," + " " + address + ","
                    lines += " " + str(self.carretailer_business_hours) + "," + " " + "['" + str(car) + "']"
                    output.write(lines)
                    output.write('\n')
                    output.close()
                else:
                    # if retailer records exist update the car stock for the retailer
                    input.close()
                    # extract the car codes from the stock.txt file
                    pattern = r'\[(.*?)\]'
                    extracted_data = re.findall(pattern, lines)
                    repl_data = str(extracted_data[0]) +",'" + str(car) +"'"
                    input_handle_retailer = open('stock.txt', 'r')
                    file_data = input_handle_retailer.read()
                    input_handle_retailer.close()
                    file_data = file_data.replace(extracted_data[0], repl_data)
                    output = open('stock.txt', 'w')
                    output.write(file_data)
                    input.close()
                    output.close()
            return True

    def get_stock_by_car_type(self,car_types):
        car_types_list =[]
        # get the car objects for car codes of the current retailer id
        for i in range(0,len(CarRetailer.car_stock_list)):
            if CarRetailer.car_stock_list[i].car_code in self.carretailer_stock:
                # get the type for the car
                check = CarRetailer.car_stock_list[i].get_car_type()
                # if the car types matches the input car type list then return the car object
                if check in car_types:
                    car_types_list.append(CarRetailer.car_stock_list[i])
        return car_types_list

    def get_stock_by_licence_type(self,licence_type):
        licence_car_list = []
        # if the licence type is "P" then get  the car objects
        if licence_type == "P":
            for car in CarRetailer.car_stock_list:
                if car.car_code in self.carretailer_stock:
                    # cehck if the car_code is prohibited vehicle
                   licence_car = car.probationary_licence_prohibited_vehicle()
                   if not licence_car:
                        licence_car_list.append(car)
        else:
            # if licence is Full or L
            for car in CarRetailer.car_stock_list:
                if car.code in self.carretailer_stock:
                    licence_car_list.append(car)
        return licence_car_list

    def car_recommendation(self):
        # chooses a random car from the carretailer_stock
        car_reco = random.choice(self.carretailer_stock)
        for each in CarRetailer.car_stock_list:
            if each.car_code == car_reco:
                return each

    def create_order(self,car_code):
        for each in CarRetailer.car_stock_list:
            # check if car code matches any car object
            check = each.found_matching_car(car_code)
            if check == True:
                obj = each
                break
        # call Order class to generate an order
        order_obj = Order(order_car = obj ,order_retailer = Retailer(self.retailer_id,self.retailer_name),order_creation_time = int(time.mktime(time.localtime())))
        # store the order details in the order.txt file
        output = open('order.txt', "a")
        order_details = str(order_obj)
        output.writelines(order_details)
        output.write('\n')
        output.close()
