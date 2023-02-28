def hextobi(string):
    ex = ''
    for s in string:
        if s.isdigit():
            b = int(s)
        else:
            b = ord(s) - ord('A') + 10
        for j in range(3,-1,-1):
            r = b & 1<<j
            if r:
                ex += '1'
            else:
                ex += '0'
    return ex

def make_codeset():
    for row in arr:
        new_code = hextobi(row)
        while '1' in new_code:
            for idx in range(len(new_code)-1,-1,-1):
                if new_code[idx] == '1':
                    new_code = new_code[:idx+1]
                    length = len(new_code) - 1
                    break
        #전처리 후 code_set에 추가
            start = len(new_code) - 1
            while start>=0:
                cnt0 = 0
                cnt1 = 0
                cnt2 = 0
                cnt3 = 0
                while start>=0 and new_code[start] == '1':
                    cnt0 += 1
                    start -= 1
                while start>=0 and new_code[start] == '0':
                    cnt1 += 1
                    start -= 1
                while start>=0 and new_code[start] == '1':
                    cnt2 += 1
                    start -= 1
                while start>=0 and new_code[start] == '0':
                    cnt3 += 1
                    start -= 1
                k = min(cnt0, cnt1, cnt2, cnt3)
                break

            code_set.add(new_code[len(new_code) - 56*k:len(new_code)])
            new_code = new_code[:len(new_code) - 56*k]

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split()) #행,열
    arr = [input().rstrip() for _ in range(N)]
    code_set = set()
    make_codeset()
    ans_lst = []
    decode = {(3,2,1,1):0, (2,2,2,1):1, (2,1,2,2):2, (1,4,1,1):3, (1,1,3,2):4,(1,2,3,1):5\
              , (1,1,1,4): 6, (1,3,1,2):7,(1,2,1,3):8,(3,1,1,2):9}
    for code in code_set:
        ans = ''
        start = len(code) - 1
        while start>=0:
            cnt0 = 0
            cnt1 = 0
            cnt2 = 0
            cnt3 = 0
            while start>=0 and code[start] == '1':
                cnt0 += 1
                start -= 1
            while start>=0 and code[start] == '0':
                cnt1 += 1
                start -= 1
            while start>=0 and code[start] == '1':
                cnt2 += 1
                start -= 1
            while start>=0 and code[start] == '0':
                cnt3 += 1
                start -= 1
            k = min(cnt0, cnt1, cnt2, cnt3)

#{'00011010001011010001101101110110111001001101000110111101'}
        for i in range(0,len(code),7*k):
            new_code = code[i:i+7*k]
            ratio = []
            v = 0
            for j in ('0','1','0','1'):
                cnt = 0
                while v<len(new_code) and new_code[v] == j:
                    cnt += 1
                    v += 1
                ratio.append(cnt)
            for idx in range(4):
                ratio[idx] //= k
            t_ratio = tuple(ratio)
            if t_ratio not in decode.keys():
                break
            else:
                ans += str(decode[t_ratio])
        ans_lst.append(ans)

    final_ans = 0
    for ans in ans_lst:
        rst = 0
        for i in range(0,7,2):
            rst += int(ans[i]) * 3
            rst += int(ans[i+1])
        if rst%10 == 0:
            for num in ans:
                final_ans += int(num)
    print(f'#{tc} {final_ans}')


