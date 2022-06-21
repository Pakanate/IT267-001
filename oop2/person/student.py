from person import Person

class Student(Person):
    def __init__(self,name,facuilty,major,year) -> None:
        super().__init__(name)
        self.facuilty = facuilty
        self.major = major
        self.year = year
    
    def welcome(self):
        super().welcome()
        print(f'Welcome to {self.facuilty} major{self.major} in {self.year}')
    
  
    


    