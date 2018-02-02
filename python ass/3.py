class Person(object):
    def _init_(self):
        pass
    def getGender(self,gender):
        print gender

class Male(Person):
    def getGender(self):
        super(Male,self).getGender("Male")

class Female(Person):
    def getGender(self):
        super(Female,self).getGender("Female")


m=Male()
m.getGender()

f=Female()
f.getGender()

