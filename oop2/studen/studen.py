class Studen:
    def __init__(self,stuid,name,major) -> None:
        self._setuid = stuid
        self._name = name
        self._major = major

    def _displayNameAndMajor(self):
        print(f'Name: {self._name}')
        print(f'Major: {self._major}')
        