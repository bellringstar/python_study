'''
Data Structure
데이터 + 연산 
각 데이터의 횽율적인 저장, 관리를 위한 구조를 나눠 놓은 것
'''

#주어진 문자열에서 숫자, 문자, 기호가 각각 몇개인지 판단하는 함수를 작성해보세요.
# def check(target_str):
#     str_count = 0
#     digit_count = 0
#     except_count = 0
#     for s in target_str:
#         if s.isalpha():
#             str_count += 1
#         elif s.isdigit():
#             digit_count += 1
#         else:
#             except_count += 1
#     return f'문자 : {str_count}, 숫자 : {digit_count}, 기호 : {except_count}'

# 문자 : 10개, 숫자 : 3개, 기호 : 7개



d = {'a' : 3, 'b' : 6, 'c' : 8, 'd' :1}
print(sorted(d.values(), key=lambda x: x))