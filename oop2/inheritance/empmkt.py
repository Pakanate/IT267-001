from employee import Employee

class EmpMKT(Employee):
    def __init__(self, id, name, salary) -> None:
        super().__init__(id, name, salary)
        self.location ='Bangkok'
        self.commision = 30
        self.department = 'Marketing'

    def add_location(self,location):
        self.location = location
    
    def add_commision(self,commision):
        self.commision = commision

    def emp_detail(self):
        print("==== Employee MKT Detail====")
        #เรียกใช้เมธอท Emp_detail ของคลาส Employee เพื่อแสดง Idและ name
        super().emp_detail() #เรียกใช้จาก employee โดยใช้Superจะได้idกับname
        print(f'location: {self.location}')
        print(f'commision: {self.commision}%')

    def mkt_salary(self):
        self._emp_salary()