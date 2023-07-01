from pet import Pet

user_pet = Pet()

pet_name = input("What is the name of your pet? ")
pet_type = input("What kind of an animal is your pet? ")
pet_age = input("How old is your pet? ")

user_pet.set_name(pet_name)
user_pet.set_animal_type(pet_type)
user_pet.set_age(pet_age)

print("Your pet's name is " + user_pet.get_name())
print("Your pet is a " + user_pet.get_animal_type())
print("Your pet is " + str(user_pet.get_age()) + " years old.")