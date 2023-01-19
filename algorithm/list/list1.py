def BublleSort(numbers):
    for i in range(len(numbers)-1, 0, -1): #4,3,2,1
        for j in range(0, i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

T = int(input())
for i in range(1, T+1):
    lenN = int(input())
    numbers = list(map(int, input().split()))
    print(f'#{i} {BublleSort(numbers)[-1] - BublleSort(numbers)[0]}')






