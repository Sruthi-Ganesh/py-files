def writing_to_file():
    try:
        input_file=raw_input("enter the inputfile name ")
        out_file=raw_input("Enter the output file ")
        in_file=open(input_file,"r+")
        
        out_file=open(out_file,"w+")
        i=1
        for line in in_file:
            print line.rstrip()
            out_file.write(line.rstrip()+"\n")
            i=i+1
        in_file.close()
        out_file.close()
        print "Successfully Written."
    except IOError,e:
        print "There was an error in running this program"
        print e

print "ct20162001781",
print "sruthibadal@gmail.com \n"    
writing_to_file()
