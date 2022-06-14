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

    def __del__(self):
        print(f'Object was destroyed')
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

    #เรียกดูclass varibaleทั้งหมด
    print(f'{Animal.__dict__}')


    #เรียกดู Intsance varibale
    print(f'{ula.__dict__}')

    peter = Animal()
    peter.new_animal("Peter", "Parrot", "green yellow red", 2)
    #เพิ่มattribute to peter
    peter.legs = 2
    print(f'Peter has {peter.legs} legs')
    print(f'{peter.__dict__}')
   
    
