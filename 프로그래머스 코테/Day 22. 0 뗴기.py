## 나의 문제풀이

def solution(n_str):
    cnt = 0
    for i in range(len(n_str)):
        if n_str[i] != '0':
            cnt = i
            break
    return n_str[cnt:]

## 다른사람의 문제풀이

def solution(n_str):
    return n_str.lstrip('0') # 이런 방법이!
