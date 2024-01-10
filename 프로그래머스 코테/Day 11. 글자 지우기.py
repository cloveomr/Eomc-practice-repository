## 나의 문제풀이

def solution(my_string, indices):
    answer = [i for i in my_string]
    for i in indices:
        answer[i] = ""
    return "".join(answer)
