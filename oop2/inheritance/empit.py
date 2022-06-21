from employee import Employee

class EmpIT(Employee):
    def __init__(self, id, name, salary) -> None:
        super().__init__(id, name, salary)
        self.skill = None
        self.experience = ""
        self.department = "IT"

    def add_skill(self, skill:str):
        self.skill = skill

    def add_experience(self,experience):
        self.experience = experience
    
    def emp_detail(self):
        print("==== Employee IT Detail====")
        #เรียกใช้เมธอท Emp_detail ของคลาส Employee เพื่อแสดง Idและ name
        super().emp_detail() #เรียกใช้จาก employee โดยใช้Superจะได้idกับname
        print(f'')
        print(f'skill: {self.experience} year(s)')

    def it_salary(self):
        self._emp_salary()
        