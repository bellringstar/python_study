# 6 
lst = [1, 3, 3, 3, 1, 1, 3]

'''
1등의 번호 출력(index +1)
1 = 가위 2 = 바위 3 = 보
1. lst를 각 그룹이 2명 이하가 될 때까지 반으로 나눈다. -> 리스트를 튜플로 변경 후 그룹화
2. 반으로 나눈 그룹에서 승자를 뽑느다. index와 번호를 스택에 쌓는다. 
3. 승자가 2명 이상이라면 index가 작은 쪽을 승자로 한다.
4. left 승자와 right 승자를 비교해 1등을 뽑는다. -> 스택 내 두 원소의 번호를 비교

i = 0 j = 2
[0,1] [2]

'''
new_lst = [(idx, lst[idx]) for idx in range(len(lst))]
rst = []
stack = []

def partition(lst, start, end):
    left = lst[start:(start+end)//2+1]
    right = lst[(start+end)//2 + 1 : end+1]
    lst = [left, right]
    if len(left)>2:
        partition(left, start, len(left) - 1)
    if len(right) >2:
        partition(right, start, len(right) - 1)
    if len(left)<=2 and len(right)<=2:
        rst.append(lst)


def win(tuple_a, tuple_b):
    if tuple_a[1] - tuple_b[1] == 1 or tuple_a[1] - tuple_b[1] == -2 :
        return tuple_a
    elif tuple_a[1] == tuple_b[1]:
        if tuple_a[0] < tuple_b[0]:
            return tuple_a
        return tuple_b
    else:
        return tuple_b
 
partition(new_lst, 0, len(lst) -1)

for upper_group in rst:
    for group in upper_group: 
        if len(group) == 2:
            stack.append(win(group[0], group[1]))  
        else:
            stack.append(group[0])        
# print(stack)
while len(stack) != 1:
    winner = win(stack.pop(), stack.pop())
    if len(stack) == 0:
        final_winner = winner
        break
    if len(stack) == 2:
        winner2 = win(stack.pop(), stack.pop())
        stack.append(winner2)
    stack.append(winner)
    

print(final_winner[0]+1)


    







