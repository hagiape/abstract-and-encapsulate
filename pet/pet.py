# Write a class named Pet, which should have the following data attributes:
# • _ _name (for the name of a pet)
# • _ _animal_type (for the type of animal that a pet is. Example values are ‘Dog’, ‘Cat’, and ‘Bird’)
# • _ _age (for the pet’s age)

# The Pet class should have an _ _init_ _ method that creates these attributes. It should also have the following methods:
# • set_name()
# This method assigns a value to the _ _name field.
# • set_animal_type()
# This method assigns a value to the _ _animal_type field.
# • set_age()
# This method assigns a value to the _ _age field.
# • get_name()
# This method returns the value of the _ _ name field.
# • get_animal_type()
# This method returns the value of the _ _animal_type field.
# • get_age()
# This method returns the value of the _ _age field.

class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
    def set_name(self, name):
        self.__age = name
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    def set_age(self, age):
        self.__age = age
    def get_name(self):
        return self.__name
    def get_animal_type(self):
        return self.__animal_type
    def get_age(self):
        return self.__age