def hanoi(N, start, to, via):
    if N == 1:
       move(1, start, to) 
    else:
        hanoi(N-1, start, via, to)
        move(N, start, to)
        hanoi(N-1, via, to, start)
def move(N, start, to):
    print(f'{N}번 원반을 {start}에서 {to}로 옮긴다.')

hanoi(3, 'A', 'C', 'B')


'''
A번 기둥의 1번 원반을 B번 기둥에 옮긴다.
A번 기둥의 2번 원반을 B번 기둥에 옮긴다.
B번 기둥의 1번 원반을 B번 기둥에 옮긴다.
A번 기둥의 3번 원반을 C번 기둥에 옮긴다.
B번 기둥의 1번 원반을 B번 기둥에 옮긴다.
B번 기둥의 2번 원반을 C번 기둥에 옮긴다.
B번 기둥의 1번 원반을 C번 기둥에 옮긴다.
'''
