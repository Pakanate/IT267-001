from empit import EmpIT
from empmkt import EmpMKT
#create objce  employee IT
mike= EmpIT("001", "mike", 60000)
mike.add_skill("Pyton, JavaSrvipt")
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()


#create objce employee MKT
anna = EmpMKT("002", "Anna", 35000)
anna.emp_detail()
anna.mkt_salary()

#พนักงานแผนการตลาดชื่อ Paul มีเงินเดือน 45000 ได้รับค่าคอมมิชชัน35% โดยทำงานอยู่ที่เชียงใหม่

paul = EmpMKT("003", "Paul", 45000)
paul.add_commision(35)
paul.add_location('Chaing-Mai')
paul.emp_detail()
paul.mkt_salary()