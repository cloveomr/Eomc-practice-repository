## 나의 문제풀이

def solution(arr, delete_list):
    answer = []
    for i in arr:
        if i not in delete_list:
            answer.append(i)
    return answer
