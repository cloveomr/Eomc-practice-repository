## 나의 문제풀이

def solution(my_string, is_suffix):
    answer = 0
    for i in range(len(my_string)):
        if my_string[i:len(my_string)] == is_suffix:
            answer = 1
            break
            
    return answer

## 다른사람 문제풀이

def solution(m, s):
    if m[-len(s):]==s: return 1
    return 0
