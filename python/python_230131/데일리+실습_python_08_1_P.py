participants =  [3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21]

'''
짝이 지어지지 않은 번호
'''
while participants:
    num = participants.pop()
    if num in participants:
        participants.remove(num)
    else:
        print(num)
        break