from studen import Studen

class ITDS(Studen):
    def __init__(self, stuid, name, major)-> None:
        super().__init__(stuid, name, major)
    
    def _displayNameAndMajor(self):
        print(f'ITDS Name: {self._name}')
        super()._displayNameAndMajor()


stu = ITDS("620108020002","Amorn",'Information Technology')
stu._displayNameAndMajor()