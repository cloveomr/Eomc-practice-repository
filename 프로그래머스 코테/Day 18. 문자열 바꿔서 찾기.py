## 나의 문제풀이

def solution(myString, pat):
    answer = []
    for i in myString:
        if i == 'A':
            answer.append('B')
        else:
            answer.append('A')
    if pat in "".join(answer):
        return 1
    else:
        return 0

## 다른사람의 문제풀이

def solution(myString, pat):
    return int(''.join(['A' if i == 'B' else 'B' for i in pat]) in myString) # myString이 아닌 pat을 변경하여 풀 수 있다!
