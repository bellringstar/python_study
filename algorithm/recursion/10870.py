#memoization
n = int(input())

def fib(n):
    global memo
    if n>=2 and len(memo)<=n :
        memo.append(fib(n-1) + fib(n-2))
    return memo[n]
memo = [0, 1]

print(fib(n))