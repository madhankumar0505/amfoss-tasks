test_cases = int(input())

for i in range(test_cases):
    string = input().split(" ")
    if string[len(string)-1] == '':
        string = string[:len(string)-1 ]

    bag_num = int(string[0])
    min_coins = int(string[1])
    bag = input().split(" ")

    if bag[len(bag)-1] == '':
        bag = bag[:len(bag)-1 ]
    
    bag = [int(i) for i in bag] 
    bag.sort()
    bag[bag_num-1] = bag[bag_num-1] - min_coins
    ans = 1
    for i in bag:
        ans *= i
    print(ans)
    
