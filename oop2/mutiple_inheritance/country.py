from geographic import Geographic
from temperature import Temperature

class Country(Geographic, Temperature) :
    def __init__(self,name,area,pop) -> None:
        self.name = name
        self.area = area
        self.population = pop

    def getpopulation(self):
        return self.population/self.area
    
    def showdetail(self):
        #แสดงสถานที่ตั้ง 
        print(f'Country: {self.name}')
        print(f'Location: {self.getcordinate()}')
        #แสดงขนาดพื้นที่
        print(f'Population: {self.population}')
        print(f'Area : {self.area}')
        print(f'Density: {self.getpopulation()}')

        #Time Zone ,Clmate , Temperature, Weather
        print(f'Timezoen: {self.gettimezone}')
        print(f'Climate:{self.getclimate()}')
        print(f'Temperture(C) : {self.getcelcius()}')
        print(f'Temperture(F): {self.getfahrenheit()}')
        print(f'Weather: {self.getweather()}')

        print('*************************************************')

