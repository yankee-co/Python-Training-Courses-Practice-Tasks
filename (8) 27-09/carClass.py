from dataclasses import dataclass
import random as r
from typing import Optional

@dataclass
class Car:
	model: str
	vendor: str
	doors_amount: int
	vin: str
	number_plate: str = None
	is_registered: bool = None

	def register(self, number_plate):
		if number_plate != None: raise ValueError
		else:
			self.number_plate = input("Enter number plate: (9 chars): ")
			print(self.vendor, self.model, 'has a number plate now: ', self.number_plate)
		self.is_registered = True

	def unregister(self, temp_number):
		self.is_registered = False
		temp_number = input("Enter new temporary number: ")
		print(self.vendor, self.model, "is unregistered.", "Temporary number: ", temp_number)
		self.number_plate = temp_number

if __name__ == '__main__':
	car1 = Car(model = "Q1", vendor = "BMW", doors_amount = 4, vin = "ZFA22300005556771")
	car2 = Car(model = "S8 2020", vendor = "Audi", doors_amount = 4, vin = "ZFA22300005556772")
	car3 = Car(model = "A6 2021", vendor = "Audi", doors_amount = 4, vin = "ZFA22300005556713")
	car4 = Car(model = "S90 2021", vendor = "Volvo", doors_amount = 4, vin = "ZFA22300005556724")
	car5 = Car(model = "228 Gran Scoupe 2021", vendor = "BMW", doors_amount = 4, vin = "ZFA22300005556735", number_plate = None)
	car6 = Car(model = "MX30 2020", vendor = "Mazda", doors_amount = 4, vin = "ZFA22300005556746")
	car7 = Car(model = "CX-30 2020", vendor = "Mazda", doors_amount = 4, vin = "ZFA22300005556757")
	car8 = Car(model = "BT-50 2018", vendor = "Mazda", doors_amount = 4, vin = "ZFA22300005556768")
	carList = [car1, car2, car3, car4, car5, car6, car7, car8]

	#Searching for mazda 2020 cars
	b = 0
	print('Mazda 2020 cars:')
	for i in carList:
		if (carList[b].model.find('2020') != -1 and carList[b].vendor == 'Mazda'):
			print(carList[b].vendor ,carList[b].model)
		b+=1
	#Unregistering car givin' temporary number
	car1.register(number_plate = None)
	print(car1.is_registered) # True
	print(car2.is_registered) # None
	car1.unregister(temp_number = car1.number_plate)
	print(car1.is_registered) # False
