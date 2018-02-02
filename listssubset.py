def subsets(x):
    if x == []:
        return [[]]
    else:
        s = [x]
        
        for i in x:
            tmp = x[:]
            tmp.remove(i)
            print "tmp: " + str(tmp)
            n = subsets(tmp)  #recursion
            print "n: " + str(n)
            for y in n:
                if y not in s:
                    s.append(y)
        print "s: " + str(s)
        return s
print subsets([1,2,3,4])
