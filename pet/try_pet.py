# Once you have written the class, write a program that creates an object of the class and 
# prompts the user to enter the name, type, and age of his or her pet. 
# This data should be stored as the object’s attributes. 
# Use the object’s accessor methods to retrieve the pet’s name, type, and age and display this data on the screen.
from pet import Pet

user_pet = Pet()

pet_name = input("What is the name of your pet? ")
pet_type = input("What kind of an animal is your pet? ")
pet_age = input("How old is your pet? ")