# def mySum(lst, sumV):
#     for value in lst:
#         sumV += value
#     return sumV

# def getDiv(N, sumV):
#     lst = []
#     for i in range(1, N+1):
#         if N % i == 0:
#             lst.append(i)
#     sumV = mySum(lst, sumV)
#     print(sumV)
#     return lst, sumV

# sumV = 0
# for i in range(15, 21):
#     print(getDiv(i, sumV))


#dict_list_sum :  딕셔너리 리스트를 받아 딕셔너리 키 'age'의 합(정수)를 반환

# def dict_list_sum(lst):
#     sumA = 0
#     for idx in lst:
#         sumA += idx['age']
#     return sumA

# sumA = dict_list_sum([{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}, {'name': 'ssafy', 'age': 14}])
# print(sumA)
     
# x = 10
# y = x
# y = 20
# print(x, y) #10 20

# xlst = [1, 2, 3]
# ylst = xlst
# ylst[1] = 100
# print(xlst, ylst) # [1, 100, 3] [1, 100, 3] 리스트 = 참조호출 아이디가 넘어간다

# print(id(x),id(y),id(xlst),id(ylst))



def all_list_sum(lst):
    sum = 0
    for i in lst:
        for j in i:
            sum += j
    return sum

print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9,10]]))