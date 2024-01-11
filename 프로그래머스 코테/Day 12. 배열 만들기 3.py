## 나의 문제풀이

def solution(arr, intervals):
    a, b = intervals[0]
    c, d = intervals[1]
    return arr[a:b+1]+arr[c:d+1]

## 다른 사람의 문제풀이

def solution(arr, intervals):
    answer = []
    for a,b in intervals: answer+=arr[a:b+1] # for문을 사용하여 리스트를 합침
    return answer
