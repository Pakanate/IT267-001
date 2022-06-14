class Car:
    brand = "Toyota"

    def __init__(self,model, colour, year , price):
        self.model = model
        self.colour = colour
        self.year = year
        self.price = price
    
    def print_detail(self):
        print(f"Model: {self.model}")
        print(f"Colour: {self.colour}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price}")
    #static method ไม่ต้องมีself
    @staticmethod
    def get_static_method(text):#มี 1 argument คือ text
        print(f"String: {text}")

    #static method จะต้องมีclass
    @classmethod
    def get_static_method(cls,text):
        print(f"This is class method{text}")
    
if __name__ == "__main__":
    my_car = Car("Cross", "White", 2022,1500000)
    #call instance method
    my_car.print_detail()
    #call static method
    Car.get_static_method("Hello Class")
    my_car.get_static_method("Good car OBject")
    #call class method
    Car.get_static_method("Go Home")