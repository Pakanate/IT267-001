from documentary_private import Documetary

m = Documetary('Mulan', 2020, 'action')
#m.__get_movie() #เราเรียก private method ไม่ได้
#print(m.__genre) #เราเรียก private attribute ไม่ได้
m.print_detail()
print(f'year : {m._Movie__year}')
#obj._ClassName__privateattribute