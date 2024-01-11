## 나의 문제풀이

def solution(arr):
    answer = []
    for i in range (len(arr)):
        if arr[i] == 2:
            answer.append(i)
    if len(answer) >= 1:
        return arr[answer[0]:answer[-1]+1]
    else:
        return [-1]

## 다른사람의 문제풀이

def solution(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)] ## arr에서 처음 2의 index를 구하고 마지막 2의 index를 구하는 코드이다.
