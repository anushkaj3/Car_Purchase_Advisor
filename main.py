from car import Car
from retailer import Retailer
from order import Order
from car_retailer import CarRetailer
import re
import time
import os
import random
import string


def main_menu():
	"""
	main menu prints the options for the user to select from

	"""
	print("a) Look for the nearest car retailer")
	print("b) Get car purchase advice")
	print("c) Place a car order")
	print("d) Exit")


def generate_test_data():
	"""
	generate_test_data loads test data into the memory and updates the stock.txt file
	"""

	#if a stock file exists , clear the file to avoid duplicate data
	check = os.path.isfile('stock.txt')
	if check :
		output = open('stock.txt',"w")
		output.close()
		output = open('order.txt',"w")
		output.close()

	retailer_id = -1
	car_codes = [] # stores the car_codes for generating unique car_codes

	for i in range(0,13):
		# generate unique car codes 6 digits and 2 alphabets
		car_num = random.randint(100000,999999)
		car_alpha = random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)
		car_code = car_alpha + str(car_num)
		# check if car code already exists, if yes generate a new code
		if car_code in car_codes:
			car_num = random.randint(100000, 999999)
			car_alpha = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
			car_code = car_alpha + str(car_num)
		car_codes.append(car_code)
		# create a list of allowed car types
		car_types = ["AWD","RWD","FWD"]
	list_retailer = []
	# creating the first retailer by calling CarRetailer class
	ob1 = CarRetailer(retailer_id,retailer_name = "Metro Traders",carretailer_address="City Rd SouthBank, VIC 3006",
					  carretailer_business_hours= (8.5,23.5),carretailer_stock=[])
	ob1.generate_retailer_id(list_retailer)
	#list_retailer.append(ob1)
	# creating first car for the retailer id 1
	car = Car(car_codes[0],car_name= "Hyundai",car_capacity=(random.randint(1,7)),car_horsepower=125,car_weight=2500,
				 car_type= random.choice(car_types))
	# update the stock.txt file with the car
	ob1.add_to_stock(car)
	# update the current stock for the retailer
	ob1.load_current_stock('stock.txt')
	# loading car 2 for the retailer 1
	car1 = Car(car_codes[1], car_name="Camaro", car_capacity=(random.randint(1, 7)), car_horsepower=115,
			  car_weight=2700,
			  car_type=random.choice(car_types))
	# update stock.txt file with car 2
	check = ob1.add_to_stock(car1)
	if not check:
		print("Car already exists in current stock")
	ob1.load_current_stock('stock.txt')
	# loading car 3 for retailer 1
	car2 = Car(car_codes[2], car_name="Camry", car_capacity=(random.randint(1, 7)), car_horsepower=145,
			  car_weight=1500,
			  car_type=random.choice(car_types))
	check = ob1.add_to_stock(car2)
	if not check:
		print("Car already exists in current stock")
	ob1.load_current_stock('stock.txt')
	# loading car 4 for the retailer 1
	car3 = Car(car_codes[3], car_name="Sedan", car_capacity=(random.randint(1, 7)), car_horsepower=155,
			  car_weight=2560,
			  car_type=random.choice(car_types))
	check= ob1.add_to_stock(car3)
	ob1.load_current_stock('stock.txt')
	if not check:
		print("Car already exists in current stock")

	# calling Car retailer class for retailer 2
	ob2 = CarRetailer(retailer_id, retailer_name="Bernie Smith Cars", carretailer_address="Maloja Av Cloundra, QLD 4551",
					  carretailer_business_hours=(9.0, 23.5), carretailer_stock=[])
	ob2.generate_retailer_id(list_retailer)
	list_retailer.append(ob2)
	# loading car 1 for the retailer 2
	car = Car(car_codes[4], car_name="Honda", car_capacity=(random.randint(1, 7)), car_horsepower=285,
			  car_weight=1650,
			  car_type=random.choice(car_types))
	check = ob2.add_to_stock(car)
	ob2.load_current_stock('stock.txt')
	if not check:
		print("Car already exists in current stock")
	# loading car 2 for the retailer 2
	car = Car(car_codes[5], car_name="Ford", car_capacity=(random.randint(1, 7)), car_horsepower=235,
			  car_weight=2750,
			  car_type=random.choice(car_types))
	check =ob2.add_to_stock(car)
	ob2.load_current_stock('stock.txt')
	if not check:
		print("Car already exists in current stock")
	# loading car 3 for the retailer 2
	car = Car(car_codes[6], car_name="Aspen", car_capacity=(random.randint(1, 7)), car_horsepower=174,
			  car_weight=2050,
			  car_type=random.choice(car_types))
	ob2.add_to_stock(car)
	ob2.load_current_stock('stock.txt')
	# loading car 4 for the retailer 2
	car = Car(car_codes[7], car_name="Alpine", car_capacity=(random.randint(1, 7)), car_horsepower=245,
			  car_weight=1050,
			  car_type=random.choice(car_types))
	check = ob2.add_to_stock(car)
	if not check:
		print("Car already exists in current stock")
	ob2.load_current_stock('stock.txt')

    # creating retailer 3
	ob3 = CarRetailer(retailer_id, retailer_name="Trade Prestige",
					  carretailer_address="Devon St Wallsend, NSW 2287",
					  carretailer_business_hours=(10.0, 23.0), carretailer_stock=[])
	ob3.generate_retailer_id(list_retailer)
	list_retailer.append(ob3)
	# loading car 1 for the retailer 3
	car = Car(car_codes[8], car_name="Audi", car_capacity=(random.randint(1, 7)), car_horsepower=255,
			  car_weight=2130,
			  car_type=random.choice(car_types))
	check = ob3.add_to_stock(car)
	if not check:
		print("Car already exists in current stock")
	ob3.load_current_stock('stock.txt')
	# loading car 2 for the retailer 3
	car = Car(car_codes[9], car_name="Aston", car_capacity=(random.randint(1, 7)), car_horsepower=345,
			  car_weight=2130,
			  car_type=random.choice(car_types))
	ob3.add_to_stock(car)
	ob3.load_current_stock('stock.txt')
	# loading car 3 for the retailer 3
	car = Car(car_codes[10], car_name="Sedan", car_capacity=(random.randint(1, 7)), car_horsepower=195,
			  car_weight=2190,
			  car_type=random.choice(car_types))
	ob3.load_current_stock('stock.txt')
	check =ob3.add_to_stock(car)
	if not check:
		print("Car already exists in current stock")
	# loading car 4 for the retailer 3
	car = Car(car_codes[11], car_name="BMW", car_capacity=(random.randint(1, 7)), car_horsepower=135,
			  car_weight=1130,
			  car_type=random.choice(car_types))
	check = ob3.add_to_stock(car)
	if not check:
		print("Car already exists in current stock")
	ob3.load_current_stock('stock.txt')



def user_option():
	"""
	User_option loads the main menu and also checks user input
	"""
	print(" ")
	print("The following menu provides you with 4 options")
	print("Please enter the option of your choice as the corresponding alphabet eg - a , b , c or d")
	print(" ")
	main_menu()
	print(" ")
	# check if user choice is valid
	user_choice = str(input("Enter your choice:"))
	user_opt = user_choice.lower().strip()
	choice = ['a','b','c','d']
	while user_opt not in choice:
		print("Invalid Input option!")
		print("Please select a valid option from the menu by entering the alphabet corresponding to the option")
		main_menu()
		user_choice = input("Enter your choice:")
		user_opt =  user_choice.lower().strip()
	return user_opt


def main():
	# load test data
	generate_test_data()
	lines = ""
	retailer_obj = []
	input_handle_retailer = open('stock.txt', 'r')
	for line in input_handle_retailer:
		line_tokens = line.split(",")

		pattern = r'[0-9]{1,2}.[0-9]'
		ex_starth = re.findall(pattern,line_tokens[4])
		start = float(ex_starth[0])
		ex_end = re.findall(pattern,line_tokens[5])
		end = float(ex_end[0])
		hours = (start,end)
		pattern1 = r"([A-Z]{3})([0-9]{4})"
		pattern2 = r"\1 \2"
		address = re.sub(pattern1, pattern2, line_tokens[3])
		address1 = line_tokens[2] +", "+address
		obj = CarRetailer(line_tokens[0],line_tokens[1],address1,
								  hours,carretailer_stock=[])
		obj.load_current_stock('stock.txt')
		retailer_obj.append(obj)
	input_handle_retailer.close()
	user_choice = user_option()
	# allow user to perform operations till they select exit
	while user_choice != 'd':

		match user_choice:
			case 'a':
				nearest = []
				# get postcode from the user
				postcode = input("Enter your postcode:")
				postcode = postcode.strip()
				# validate postcode
				while not (postcode.isnumeric() and (len(postcode)==4)):
					print("Enter a valid postcode!")
					print("Postcodes consist of 4 numbers ")
					print(" ")
					postcode = input("Enter your postcode:")
					print(" ")
				# call the get_postcode_distance to check for the smallest postcode difference
				for ret_obj in retailer_obj:
					nearest.append(ret_obj.get_postcode_distance(int(postcode)))
				# check for the smallest postcode from the postcode differences
				minimum = min(nearest)
				# print the retailer details for the nearest retailer
				for i in range(0,len(retailer_obj)):
					if nearest[i]== minimum :
						print(" The Retailer Closest to you is :")
						print("RETAILER ID : ",retailer_obj[i].retailer_id)
						print("RETAILER NAME : ",retailer_obj[i].retailer_name)
						print(" ")
				user_choice = user_option()
			case 'b':
				cur_obj =""
				# list the available retailer id's and retsiler name
				print("Listed below are the available retailers, Retailer Id and Retailer Name")
				print("In order to proceed you would need to select a reatiler.")
				for ret_obj in retailer_obj:
					print("Retailer ID :", ret_obj.retailer_id)
					print("Retailer Name: ",ret_obj.retailer_name)
					print(" ")
				user = input("Enter the RETAILER ID of your choice from the retailers displayed above: ")
				user = user.strip()
				for ret_obj in retailer_obj:

					if str(ret_obj.retailer_id) == user:
						cur_obj = ret_obj
				# validate user entered retailer id
				while not (user.isnumeric() and cur_obj != ""):
					print("Please enter a valid retailer Id from the retailer ID's displayed above")
					user = input("Enter the RETAILER ID of your choice from the retailers displayed above: ")
					user = user.strip()
					for ret_obj in retailer_obj:

						if str(ret_obj.retailer_id) == user:
							cur_obj = ret_obj
				# provide the user with a sub menu to choose from for the retailer selected
				print("Below is a sub menu ")
				print("Please choose the option you would like t proceed with for your chosen retailer ")
				print(" ")
				print("""
				1) Recommend a car
				2) Get all cars in stock
				3) Get cars in stock by car types (the car types is a list of strings, e.g.,[“AWD”, “RWD”])
				4) Get probationary licence permitted cars in stock""")
				print(" ")
				try:
					user_smenu = int(input("Enter an option"))
					# validate the user entered option for the sub menu
					while user_smenu < 1 or user_smenu > 4:
						print("Please enter the valid option")
						print("""
										1) Recommend a car
										2) Get all cars in stock
										3) Get cars in stock by car types (the car types is a list of strings, e.g.,[“AWD”, “RWD”])
										4) Get probationary licence permitted cars in stock
										
										""")
						user_smenu = int(input("Enter an option"))
					match user_smenu:
						case 1:
							# call the car_recommendation method to select a random car from the current tsock
							rand_car = cur_obj.car_recommendation()
							print("Retailer ID :",cur_obj.retailer_id)
							print("Retailer Name :",cur_obj.retailer_name)
							print("Car Code",rand_car.car_code)
						case 2:
							# call the get_all_stock method to get the current stock of retailers
							car_stock = cur_obj.get_all_stock()
							print("Retailer ID :", cur_obj.retailer_id)
							print("Retailer Name :", cur_obj.retailer_name)
							for each in car_stock:
								print("Car code",each.car_code)
						case 3:
							# create a list of allowed data types
							car_available = ["AWD","RWD","FWD"]
							car_types =[]
							not_valid = 1
							# ask the user to enter preffered car types
							print("The available car types are AWD, RWD and FWD")
							print("To select car's of the above types, please enter 1 or more of your prefered car types")

							car_type = input("Enter each car type with a space separating them  eg: AWD RWD")
							car_input = car_type.split(" ")
							for each in car_input:
								if each == '':
									car_input.remove(each)
							for each in car_input:
								car_types.append(each.upper())
								# validate user entered car types
							while(not_valid):
								for each in car_types:
									if each not in car_available:
										print("Enter the valid car types")
										print("The allowed car types are AWD,RWD and FWD")
										car_type = input("Enter each car type with a space separating them  eg: AWD RWD")
										car_input = car_type.split(" ")
										for each in car_input:
											if each == '':
												car_input.remove(each)
										for each in car_input:
											car_types.append(each.upper())
										not_valid = 1
										break
									else :
										not_valid = 0
								# call get_stock_by_car_types to get the car types as per entered by the user
								car = cur_obj.get_stock_by_car_type(car_types)
								for each in car:
									print("Car codes and their type is displayed below ")
									print("Car Code:",each.car_code)
									print("Car Type: ",each.car_type)

						case 4:
								print("Retailer ID :", cur_obj.retailer_id)
								print("Retailer Name :", cur_obj.retailer_name)
								# call the get_stock_by_licence_type to print the probationarty licence permitted cars
								lic_type = cur_obj.get_stock_by_licence_type("P")
								if not lic_type:
									for each in lic_type:
										print("Car codes of cars that are permitted by probationary licence")
										print("Car code:",each.car_code)
								else:
									print("There are no cars that are restricted by probationary licence")
				except ValueError:
					print("Invalid Input type")
					print("Please enter the number corresponding to your option")

				user_choice = user_option()
			case 'c':
				cur_obj = ""
				print("To order a car enter the Retailer Id and Car Code of the car of your choice")
				order = input("Enter the Retailer Id first and then the Car code separated by a space  ")
				ord_dets = order.split(" ")
				# validate the retailer id and car code entered by user to create an order
				for each in ord_dets:
					if each == '':
						ord_dets.remove(each)
				order_retailer = ord_dets[0]
				order_car = ord_dets[1]
				for each in retailer_obj:
					if str(each.retailer_id) == order_retailer:
						cur_obj = each
				while not ( cur_obj != "" ):
					#and (order_car in cur_obj.carretailer_stock)
					print("Enter a valid Retailer ID and Car Code")
					order = input("Enter the Retailer Id first and then the Car code separated by a space  ")
					ord_dets = order.split(" ")
					for each in ord_dets:
						if each == '':
							ord_dets.remove(each)
					order_retailer = ord_dets[0]
					order_car = ord_dets[1]
					for each in retailer_obj:
						if each.retailer_id == int(order_retailer):
							cur_obj = each
				# ibtain currrent time to check if retailer works at the current time
				cur_time = time.strftime("%H:%M")
				cur = cur_time.split(":")
				ck_time = ((int(cur[0]) * 60) + int(cur[1])) / 60
				check = cur_obj.is_operating(ck_time)
				if not check:
					print("Retailer does not work at the current time")
				else:
					# update the carretailer stock and stock.txt file
					check_remove =cur_obj.remove_from_stock(order_car)
					if not check_remove:
						print("THE CAR DOES NOT EXIST IN THE CURRENT STOCK")
						print(" ")
						print("Enter the correct Car Code or choose a different car")
					else:
						# create order for the car
						cur_obj.create_order(order_car)
						print("Congratulations !!!! an order has been created")
				user_choice = user_option()


if __name__ == "__main__":
	main()