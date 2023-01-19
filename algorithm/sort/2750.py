T = int(input())
lst = []
for i in range(T):
    num = int(input())
    lst.append(num)

lst.sort()
for num in lst:
    print(num)
