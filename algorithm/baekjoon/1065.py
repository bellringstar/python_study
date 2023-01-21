import sys
input = sys.stdin.readline
#1<=X<=N 한수의 개수. 어떤 수의 자리수 끼리 등차수열 
#1 ~ 99까지는 전부 한수 ex)111 = 한수 123=한수 135 =한수 109 =한수X
N = int(input())
rst = 99
for i in range(100,N+1):
    s = str(i)
    #'100' '1111
    # if s[1] - s[0] == s[2] - s[1] == s[3]-s[2] :
    #     rst +=1
    for idx in range(s):
         

