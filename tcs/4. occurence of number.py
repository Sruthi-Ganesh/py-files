def occurrence(l,num):
    if num in l:
        print "Yes, Present"
    else:
        print "No, Not Present"
    
def get_list():
    print "Enter a number, to end enter -99999 "
    numbers=[]
    while True:
        num=int(raw_input())
        if(num==-99999):
            break;
        numbers.append(num)
    return numbers


print "ct20162001781",
print "sruthibadal@gmail.com \n"
l=get_list()
num=int(raw_input("Enter the number to search "))
occurrence(l,num)
        


