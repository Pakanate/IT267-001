class Student():
    def __init__(self,id:str,name:str,major:str) -> None:
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
    John.display_detail()
