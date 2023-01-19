# fn_d(91) 
# 출력 예시 
# 101


def fn_d(n):
    n = str(n)
    sum = 0
    for word in n:
        sum += int(word)
    sum += int(n)
    return sum


def is_selfnumber(n):
    for i in range(1,n):
        if fn_d(i) == n:
            return False
                
    else:
        return True

print(is_selfnumber(21))

#if fn_d(a) == fn_d(b) -> not selfnumber

# 1 2 4 8 16 23 28 ....
# 2 4 8 ....
# 3 6 12 15 21 24 30....
# 4 8 16 23 28 .....
# 5 10 11 13 17 25 ...
# 7 14 19 ...
# 8 16 23 28 ....
# 9 18 27 36 ....
# 10 11 13 ....

