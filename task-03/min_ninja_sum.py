#Didnt work as expected :(
test_cases = int(input())

def min_ninja_sum(x, i):
        Sum=0
        for i in x:
            Sum += int(i)
        return Sum
    
for test in range(test_cases):
    lst = input().split(" ")
    x = lst[0]
    j = int(lst[1]) 
    mnslst = []
    ns0 = 0
    
    for start in range(len(x)-j+1):
        
        a = x[start:start+j]

        ns = min_ninja_sum(a,j)
        if ns > 0:
            mnslst.append(abs(ns-ns0))
            
        ns0 = ns
    
    if len(mnslst)==0:
        print(-1)
    else:
        print(min(mnslst))
