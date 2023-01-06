def pat(p):
    for i in range(1,p+1):
            for j in range(1,i+1):
                print(j * i,end='  ')
            print("\n")
p=int(input("enter number of rows: "))
pat(p)
