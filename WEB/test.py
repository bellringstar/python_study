A = int(input())
B = int(input())
C = int(input())

val = str(A * B * C)

for i in range(10):
    print(val.count(str(i)))