## 나의 문제풀이

def solution(myString, pat):
    cnt = 0
    for i in range(len(myString)):
        if pat == myString[i:len(pat)+i]: # 이부분을 myString[i:].startswith(pat) 이렇게 바꿀 수도 있다고 한다.
            cnt += 1
    return cnt
