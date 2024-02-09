## 나의 문제풀이

def solution(arr, n):
    for i in range(len(arr)):
        if len(arr) % 2 == 0:
            if i %2 != 0:
                arr[i] += n
        else:
            if i % 2 == 0:
                arr[i] += n
    return arr

## 다른사람의 문제풀이

def solution(arr, n):
    N=len(arr)
    if N%2:
        for i in range(0,N,2): arr[i]+=n
    else:
        for i in range(1,N,2): arr[i]+=n
    return arr
