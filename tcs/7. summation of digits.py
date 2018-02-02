def summation(num):
    sum=0
    while num>0:
        n=num%10
        sum+=n;
        num/=10
    print sum

print "ct20162001781",
print "sruthibadal@gmail.com \n"
num=int(raw_input("Enter a integer to print the sum "))
summation(num)
