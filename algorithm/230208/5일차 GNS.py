import sys
sys.stdin = open('GNS_test_input.txt', 'r')

def check(key):
    lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    num_dict = dict(enumerate(lst))
    num_dict = {v:k for k,v in num_dict.items()}
    return num_dict[key]

T = int(input())
for tc in range(1, T+1):
    t, l = input().split()
    l = int(l)
    num_arr = input().split()
    num_arr.sort(key=check)
    print(f'{t}')
    print(*num_arr)

