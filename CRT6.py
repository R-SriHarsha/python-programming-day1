A,B,C,D=map(int,input().split(" "))

if (A-C)==(B-D):
    print("any")
elif (A-C)>(B-D):
    print("buy B")
else:
    print("buy A")
    
