## 나의 문제풀이

def solution(arr):
    for i in range(len(arr)):
        if arr[i] >= 50 and arr[i] % 2 == 0:
            arr[i] = arr[i] // 2
        elif arr[i] < 50 and arr[i] % 2 != 0:
            arr[i] = arr[i] * 2
    return arr

# arr를 바꾸는 것보단 다른 빈 리스트를 만들어서 값을 추가하는 형식으로 가는 편이 더 좋았을 것 같다.
