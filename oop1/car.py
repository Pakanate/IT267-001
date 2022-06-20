from pyexpat import model


class car:
    #class attribute
    brand = "Toyota"

    # parameterized constructor
    def __init__(self,model, colour, year, price):
        #instace attribute
        self.model = model
        self.colour = colour
        self.year = year
        self.price = price

    #instane method
    def print_detail(self):
        print(f"Brand: {self.brand}")
        print(f"Model = {self.model}")
        print(f"Colour = {self.colour}")
        print(f"Year = {self.year}")
        print(f"Price = {self.price:,.2f}")

    @staticmethod
    def get_class_detail():
        print("This is a car class")

#create object
my_car = car("Cross","Silcer", 2021, 989000)
my_car.print_detail()
#static method
car.get_class_detail()
my_car.get_class_detail()