# Next, design a program that creates a Car object then calls the accelerate method five times. 
# After each call to the accelerate method, get the current speed of the car and display it. 
# Then call the brake method five times. 
# After each call to the brake method, get the current speed of the car and display it.

from car import Car

my_car = Car(2006, "Honda")

my_car.accelerate()
print("The car speed is currently "+ str(my_car.get_speed()))

my_car.accelerate()
print("The car speed is currently "+ str(my_car.get_speed()))

my_car.accelerate()
print("The car speed is currently "+ str(my_car.get_speed()))

my_car.accelerate()
print("The car speed is currently "+ str(my_car.get_speed()))

my_car.accelerate()
print("The car speed is currently "+ str(my_car.get_speed()))

my_car.brake()
print("The car speed is currently "+ str(my_car.get_speed()))

my_car.brake()
print("The car speed is currently "+ str(my_car.get_speed()))

my_car.brake()
print("The car speed is currently "+ str(my_car.get_speed()))

my_car.brake()
print("The car speed is currently "+ str(my_car.get_speed()))

my_car.brake()
print("The car speed is currently "+ str(my_car.get_speed()))