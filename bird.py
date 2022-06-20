#global variable
bird_type ='parrot'

class Bird:
    #class variable
    bird_name = 'Peter'

    def __init__(self, color) -> None:
        #instance variable
        self.color = color
        country = 'Thailand'
        print(country)

    def show(self):
        return f'{bird_type} {Bird.bird_name} has {self.color}'

if __name__ == '__main__':
    print(f'*****{bird_type}*****')#เรียกใช้ global variable
    my_bird = Bird('Red,Yellow')
    print(my_bird.show())

    #เรียก class variable
    #print(bird_name) error\
    #เรียก class variable ต้องมีชื่อclassด้วย
    print(Bird.bird_name)
    #เรียก class variable เรียกผ่านชื่อวัตถุได้ด้วย
    print(my_bird.bird_name)

    #เรียก instance variable
    #  print(Bird.color)#error
    
    #เรียก ต้องมีชื่อวัตถุ.isinstance_variable
    print(my_bird.color)

