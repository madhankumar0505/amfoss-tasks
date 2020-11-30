test_case = int(input())

for i in range(test_case):
    k = int(input())
    string = input()
    list1 = string.split(" ")
    if k >= len(list1):
        print(-1)
    else:
        reqword = list1[k]
        asciival = 0
        for letter in reqword:
            asciival += ord(letter)
        print(asciival)
