def reading(fruit):
    try:
        i=0
        in_file=open("input.txt","r+")
        for line in in_file:
            for word in line.split():
                word1=word.lower()
                if(i==1):
                    print word
                    break;
                if(word1==fruit):
                    i=1;
                    continue
            if(i==1):
                break;
                
        in_file.close()

    except IOError,e:
        print "Error:IO " + e


y=raw_input("Enter the fruit in lowercase")
reading(y)
