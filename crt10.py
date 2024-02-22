N,x=map(int,input().split(" "))
if N<x:
    print("0")
if N>x:
    if((N-x)%4==0):
        print((N-x)//4)
    else:
        print(((N-x)//4)+1)

