class Student():
    #major:str = "IT"
    #major = "IT"
    #major: "IT" จะERROR
    def __init__(self,id:str,name:str,major:str = 'IT') -> None:
        self.id = id
        self.name = name
        self.major = major

    def display_detail (self):
        print("____________")
        print(f"ID: {self.id}")
        print(f"NAME: {self.name}")
        print(F"MAJOR: {self.major}")
        print("____________")
    def __del__(self):
        print(f'Object was destroyed')
if __name__== "__main__":
    Jesssica = Student("111", "Jessice", "IT")
    Jesssica.display_detail()
    John = Student("112", "John", "MKT")
    amy = Student('113', 'Amy')

    Jesssica.display_detail()
    John.display_detail()
    amy.display_detail()