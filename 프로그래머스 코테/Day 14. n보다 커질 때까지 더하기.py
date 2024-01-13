## 나의 문제풀이

def solution(numbers, n):
    result = 0
    for i in numbers:
        result += i
        if result > n:
            return result

## 다른사람의 문제풀이

def solution(numbers, n):
    answer = 0
    i=0
    while answer<=n: # 나는 for문을 썼지만 while문을 쓰는 방법도 있다!
        answer+=numbers[i]
        i+=1
    return answer
