class Animal:
    #class varaible
    animal = "cat"

    def new_animal(self,name:str,breed:str,colour:str,age:int):
        #instance variable
        self.name = name
        self.breed = breed
        self.colour= colour
        self.age = age

    def print_detail(self):
        print(f"*****************")
        print(f"Name: {self.name}")
        print(f"animal: {self.animal}")
        print(f"Breed: {self.breed}")
        print(f"colour: {self.colour}")
        print(f"age: {self.age}")

#create object
if __name__ == "__main__":
    Animal.animal = "FISH"
    ula = Animal()
    ula.animal = "DOG"
    ula.new_animal("Ula","Scottish","White",1)
    ula.print_detail()

    drac = Animal()
    drac.new_animal("drac","Scottish","White",1)
    drac.print_detail()
    drac.breed = "CATFISH"
    drac.print_detail()


    #เรียกดูข้อมูลของ object ผ่านทางชื่อclass
    Animal.print_detail(ula) #เหมือน ula.print_detail()
    Animal.print_detail(drac)#เหมือน drac.print_detail()
    


