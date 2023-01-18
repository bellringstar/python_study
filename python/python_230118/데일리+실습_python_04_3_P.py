# 입력 예시
# [1, 1, 3, 3, 0, 1, 1]

# 출력 예시
# [1, 3, 0, 1]


# 0~9로 이루어진 리스트/ 연속으로 나타나는 숫자 = 1개만 남기고 삭제/ 기존 순서 유지
lst = [1, 1, 3, 3, 0, 1, 1, 8, 9, 9]
def remove_list(lst):
    res = []
    for i in lst:
        if not res:
            res.append(i)
        elif res[-1] != i:
            res.append(i)
            
    return res
print(remove_list(lst))
