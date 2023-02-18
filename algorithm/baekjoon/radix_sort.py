def radixsort(lst):
    #자리수를 알기 위해 최대값 찾기
    max_num = max(lst)

    #counting sort를 이용해 자리수 기준 정렬
    exp = 1
    while max_num // exp > 0:
        lst = countingsort(lst, exp)
        exp *= 10 #1->10->100... 의 자리로 올려가며 정렬

    return lst

def countingsort(lst, exp):
    #초기화 자리수 기준이기 때문에 0~9만 존재
    count = [0] * 10
    output = [0] * len(lst)

    #자리수에 따른 count
    for num in lst:
        count[(num // exp) % 10] += 1

    #위치 계산을 위한 누적합
    for i in range(1, 10):
        count[i] += count[i-1]

    i = len(lst) -1
    while i >= 0:
        idx = (lst[i]//exp) % 10
        output[count[idx]-1] = lst[i]
        count[idx] -= 1
        i -= 1

    return output


'''
radix sort와 counting sort

counting sort는 간단하지만 O(n+k)이기 떄문에 value의 크기에 영향을 크게 받는다
radix sort는 counting sort를 내부에서 사용하지만 value의 크기에 관계 없이 선형 시간안에 정렬할 수 있다는 장점이 있다.

정렬해야 하는 데이터 수가 너무 많다면 radix sort를 고려해보자
'''