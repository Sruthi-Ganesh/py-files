class student:
    def __init__(self,roll,name,score):
        self.rollnumber=roll
        self.name=name
        self.score=score
    def calculate_grade(self):
        if(self.score>=80):
            print 'Grade A'
        elif(self.score>=60):
            print 'Grade B'
        elif(self.score>=50):
            print 'Grade C'
        else:
            print 'Grade F'

print "ct20162001781",
print "sruthibadal@gmail.com \n"            
rollnumber=int(raw_input('Enter rollnumber '))
name=raw_input('Enter name ')
score=int(raw_input('Enter score '))
stud=student(rollnumber,name,score)
stud.calculate_grade()
