## 나의 문제풀이

def solution(arr):
    t = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    cnt = 0
    for i in t:
        cnt = i - len(arr)
        if cnt >= 0:
            break
    return arr + [0] * cnt
