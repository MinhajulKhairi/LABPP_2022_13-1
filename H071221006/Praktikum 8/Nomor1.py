#Nomor1

class Person:
    def __init__(self, name, age, isMale):
        self.name = name
        self.age = age
        self.isMale = isMale
        if isMale:
            self.gender = 'male'
        else:
            self.gender = 'female'

    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def setAge(self,age):
        self.age = age
    def getAge(self):
        return self.age
    def setGender(self,isMale):
        if isMale:
            self.gender = 'male'
        else:
            self.gender = 'female'
    def getGender(self):
        return self.gender 

person = Person("ajul", 18, True)
print(person.getName())
print(person.getAge())
print(person.getGender())
