print "ct20162001781",
print "sruthibadal@gmail.com \n"
x=int(raw_input("Enter a number: "))
if(x<1):
    print "Please, Enter a number greater than 1"
elif (x<=3):
    print "Prime"
for i in range(2,x/2):
    if(x%i==0):
        print "Composite"
        break;
else:
    print "prime"

        
    
      
