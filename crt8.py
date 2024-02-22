A,B,C,D=map(int,input().split(" "))

if (A-A*C//100)==(B-B*D//100):
    print("any")
elif (A-A*C//100)>(B-B*D//100):
    print("buy B")
else:
    print("buy A")
    
