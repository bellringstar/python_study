T = int(input())

for test in range(T):
    str1 = input(); N = len(str1)
    str2 = input(); M = len(str2)
    #str1의 문자마다 str2에서 카운트 str1:count 딕셔너리
    #그 후 정렬해서 가장 많은 글자의 value 출력
    count_dict = {}
    for s in str1:
        count_dict[s] = str2.count(s)
    sorted_dict = sorted(count_dict.items(), key=lambda x:x[1])
    print(f'#{test+1} {sorted_dict[-1][1]}')
