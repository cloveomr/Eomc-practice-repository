## 나의 문제풀이

def solution(myString):
    answer = []
    for i in myString:
        if i == 'a' or i == 'A':
            answer.append(i.upper())
        else:
            answer.append(i.lower())
    return "".join(answer)

## 다른사람의 문제풀이

def solution(myString):
    return myString.lower().replace('a', 'A') # replace를 쓰면 엄청 간단했다... 충격
