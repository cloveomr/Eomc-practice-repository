## 나의 문제풀이

def solution(arr, queries):
    for i, j in queries:
        for k in range(i, j+1):
            arr[k] = arr[k] + 1
    return arr
