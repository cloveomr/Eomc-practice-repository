## 나의 문제풀이

def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if i % 2 == 0:
            answer.append(strArr[i].lower())
        else:
            answer.append(strArr[i].upper())
    return answer

## 다른사람의 문제풀이

def solution(strArr):
    return [s.lower() if i % 2 == 0 else s.upper() for i, s in enumerate(strArr)] ## enumerate() 함수를 쓰면 코드를 더 간략화할 수 있다!
