'''
Queue
FIFO: First In First Out #선입선출
일상생활에서 대기열과 비슷한 상태 가장 먼저 온 앞사람이 먼저 나간다
front = rear = -1
rear = 마지막으로 저장한 위치
front = 삭제한 위치
front와 rear가 같은 자리를 가리키게 된다 = 비어있다.

원형큐
front = rear = 0
front와 rear의 위치가 배열의 마지막 인덱스인 n-1를 가리킨 후 그 다음에는 논리적 순환을 이루어 배열의
처음으로 이동

공백상태와 포화상태 구분을 위해 fron가 있는 자리는 사용하지 않고 항상 빈자리로 둠

enqueue rear = (rear+1) mod n
dequeue front = (front+1) mod n

꽉차있다 -> (rear + 1) % n == front
비어있다 -> front == rear
'''
