## 나의 문제풀이

def solution(arr):
    answer = []
    for i in arr:
        for j in range(i):
            answer.append(i)
    return answer

## 다른사람의 문제풀이

def solution(arr):
    answer = []
    for num in arr:
        answer += [num] * num
    return answer
