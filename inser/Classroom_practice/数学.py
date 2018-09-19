i=0
while i<=9:
    j=0
    while j<=i:
        print("%d*%d=%d\t"%(j,i,j*i),end="")
        j+=1
    print("")
    i+=1
