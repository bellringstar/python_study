rst = [1, 3]

N = int(input())

def paper(N):
    global rst
    if N>2 and len(rst)<N:
        rst.append(paper(N-1)+2*paper(N-2))
    return rst[N-1]

print(paper(N))

