# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

lst = input().split(" ")
def group_anagrams(lst):
    rst = []
    while lst:
        mini_lst = [lst[0]]
        for i in range(1,len(lst)):
            if sorted(lst[0]) == sorted(lst[i]):
                mini_lst.append(lst[i])
        rst.append(mini_lst)
        for idx in mini_lst:
            lst.remove(idx)
    return rst      

print(group_anagrams(lst))

'''1.애너그램 판정. sorted('eat') == sorted('tea')
2.빈 리스트에 추가, 추가된 인덱스 리스트에서 삭제
3.만들어진 리스트를 또 다른 빈 리스트에 추가'
4.반복'''
