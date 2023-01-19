#상위 k명 중 가장 낮은 점수.

def cut():
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort(reverse=True)
    return scores[k-1]


print(cut())