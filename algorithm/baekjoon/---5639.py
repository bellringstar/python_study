import sys,heapq
input = sys.stdin.readline
tree = [0] * 10001

size = 0
def enque(lst,item):
    global size
    size += 1
    lst[size] = item

