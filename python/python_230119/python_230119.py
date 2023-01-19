# fruits = input("과일봉지 :")
# fruits = fruits.lower()
# fruits = fruits.split(',')

# fruits = input().lower().split(',')
# if fruits == ['']:
#     fruits = []
# else:
#     for idx in range(len(fruits)):
#         if 'rotten' in fruits[idx]:
#             fruits[idx] = fruits[idx].replace('rotten','')

# print(fruits)

# fruits = input("과일봉지 :")
# fruits = fruits.lower()
# fruits = fruits.split(',')

# for i in range(len(fruits)):
#     if 'rotten' in fruits[i]:
#         fruits[i] = fruits[i].replace("rotten","")
        

       
# print(fruits)

# map(func, iterable)
# def my_magic_func(n):
#     return n * 10

# my_list = [1, 2, 3, 4, 5]
# print(list(map(my_magic_func, my_list)))

#filter(func, iterable)
# func을 각각 적용해 True 일 때만 반환
# def odd(n):
#     return n % 2
# numbers = [1, 2, 3, 4, 5]
# result = list(filter(odd, numbers))
# print(result)

#zip(*iterables)
# name_list = ['신동민', '서재현', '박영서', '이태성', '정예원']
# age_list = [17, 18, 22, 13, 18]
# for each in zip(name_list, age_list):
#     print(each)  #('신동민', 17), ('서재현', 18) .....

#lambda function
#print((lambda x: x * x)(4)) # 16 

# map_obj = map(lambda n: n * 10, [1, 2, 3])
# rst = list(map_obj)
# print(rst)

#recursive function
'''자기자신 호출 = 종료조건 + 
다음 과정이 이전 과정과 같으며 크기만 하나 줄어든 상태
재귀 계산은 마지막 종료조건부터 다시 거슬러 올라간다.'''
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)
    

# * packing/unpacking -> packing -> 리스트로 / unpacking -> 튜플로

# def test1(*args):
#     return

# def test2(**kwargs):
#     return

# 모듈 = ~~.py python file
''' 여러 함수들을 모아놓은 파일 -> 이것을 뭉쳐 놓은것 = 패키지 (폴더) ->
 패키지를 뭉쳐 놓은 것 = 라이브러리(폴더)'''



