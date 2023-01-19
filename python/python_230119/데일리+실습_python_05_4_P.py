# num_list = [4, 4, 7, 8, 10, 4]
# sum_of_repeat_number(num_list)

# 출력 예시 
#  25

def sum_of_repeat_number(lst):
    sum = 0
    for num in lst:
        if lst.count(num) == 1:
            sum += num
    return sum

print(sum_of_repeat_number([4, 4, 7, 8, 10, 10]))
