## 나의 문제풀이

def solution(myString):
    answer = []
    for i in myString.split('x'):
        if i != "":
            answer.append(i)
    answer.sort()
    return answer

## 다른사람의 문제풀이

def solution(myString):
    return sorted(ch for ch in myString.split('x') if ch) # 리스트 컴프리헨션에 대해 알 수 있었다
