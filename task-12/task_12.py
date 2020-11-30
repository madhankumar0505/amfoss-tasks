import math
a=input("Enter number of test cases :")
a=int(a)
for i in range(a):
  
    b = input("Enter b value :")
    c = input("Enter c value :")
    b=int(b)
    c=int(c)
    x=[]
    f=[]
    def calculate(b,c):
        for x in range(1,91):
            x=x/57.29
            f.append((x*x+b*x+c)/(math.sin(x)))
        return min(f)
    print(calculate(b,c))
