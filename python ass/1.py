class prog_lang:
    
    def _init_(self):
        self.prog_list=[]
    def getlanguages(self):
        self.prog_list=[]
        x = int(raw_input("Enter the number of languages known for student "  ))
        for j in range(0,x):
            language=raw_input("Enter the languages name ")
            self.prog_list.append(language)
    def consilidated(self):
        str1 = ','.join(self.prog_list);
        return str1
    def common(self,obj2,obj3):
        for s in self.prog_list:
            for t in obj2.prog_list:
                for u in obj3.prog_list:
                    if(s==t and s==u):
                        print s
        
      
stud1 = prog_lang()
stud2 = prog_lang()
stud3 = prog_lang()

stud1.getlanguages()
stud2.getlanguages()
stud3.getlanguages()


print ("Enter 1 for consilidated and 2 for common ")
x = int(raw_input())
if(x==1):
    print stud1.consilidated()
    print stud2.consilidated()
    print stud3.consilidated()
elif(x==2):
    stud1.common(stud2,stud3)
