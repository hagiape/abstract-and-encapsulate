class Car:
    def __init__(self, year_model = 0, make = "N/A", speed = 0):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed
    
    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed
    
    def get_year_model(self):
        return self.__year_model
    
    def get_make(self):
        return self.__make