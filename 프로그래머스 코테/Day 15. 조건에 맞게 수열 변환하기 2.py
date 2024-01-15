## 나의 문제풀이

def solution(arr):
    cnt = 0
    while True:
        answer = arr[:]
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] = arr[i] // 2
            elif arr[i] < 50 and arr[i] % 2 != 0:
                arr[i] = arr[i] * 2 + 1
        cnt += 1
        if answer == arr:
            break
    return cnt - 1
