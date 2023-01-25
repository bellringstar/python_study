#1 반복문 사용
def sum_of_digit(n):
    sumD = 0
    for s in str(n):
        sumD += int(s)
    return sumD


#2 반복문 미사용
def sum_of_digit(n):
    sumD = n%10
    if n//10 == 0:
        return sumD
    return sumD + sum_of_digit(n//10)


