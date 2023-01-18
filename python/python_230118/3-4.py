'''세 변의 길이 입력
case1. 세 변의 길이가 같다
case2. 두 변의 길이가 같다.
case3. 피타고라스 ->직사각형
case4. 일반삼각형
case5. 삼각형X : 짦은 두 변의 길이의 합이 가장 긴 변의 길이보다 크다 = 삼각형'''

s_string = sorted(list(map(int, input().split())))

if  s_string[2] > s_string[0] + s_string[1]:
    print('삼각형이 아닙니다.')
else:
    if s_string[0] == s_string[1] == s_string[2]:
        print('정삼각형')
    elif s_string[1] == s_string[0]:
        print('이등변삼각형')
        if s_string[2] ** 2 == s_string[0] ** 2 + s_string[1] ** 2:
            print('동시에 직각삼각형')
    elif s_string[2] ** 2 == s_string[0] ** 2 + s_string[1] ** 2:
        print('직각삼각형')    
    else:
        print('삼각형')


