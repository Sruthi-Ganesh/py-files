def reverse_num(num):
    rev=0;
    while num>0:
        n=num%10
        rev=rev*10+n
        num=num/10
    print rev


print "ct20162001781",
print "sruthibadal@gmail.com \n"
num=int(raw_input("Enter a integer to reverse it "))
reverse_num(num)
