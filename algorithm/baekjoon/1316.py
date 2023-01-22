#그룹단어 ex)ccazzzzbb = 그룹단어, kin = 그룹단어, abbab = 그룹단어 X
#s = ccazzb
#0번단어 1번단어... 다른단어 나올떄까지 비교 다른단어 나온다 ex ccc/azc c-> 리스트 추가/다음부터 또 반복 
#하지만 해당 단어가 이미 리스트에 존재 -> 그룹단어 X

import sys
input = sys.stdin.readline

T = int(input())
counter = 0
for i in range(T):
    s = input().rstrip()
    lst = []
    for i in range(len(s)-1): #0,1,2,3,4,5
        if s[i] == s[i+1]: # i=4 s[4](z) == s[5](c)
            continue
        else:
            lst.append(s[i])
            if s[i+1] in lst:
                counter +=1 
                break
print(T-counter)

        

