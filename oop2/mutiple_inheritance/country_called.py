from country import Country

#create countryies

#thailand lat = 13.764919, long =100.483333
#population = 70,078,203
#area = 513,120
#temp = 32c
c1 = Country('Thiland', 513120, 70078203)
c1.setcordinate(13.764919,100.5360959)
c1.setcelcius(32)
c1.showdetail()

c2 = Country('Ruissa', 17100000, 144000000)
c2.setcordinate(58.000000,56.316666)
c2.setcelcius(24)
c2.showdetail()

c3 = Country('ukraine', 603548, 44000000)
c3.setcordinate(48.3794,31.1656)
c3.setcelcius(20)
c3.showdetail()
