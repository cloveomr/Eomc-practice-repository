## 나의 문제풀이

def solution(todo_list, finished):
    answer = []
    for i in range(len(finished)):
        if finished[i] == False:
            answer.append(todo_list[i])
    return answer

## 다른사람의 문제풀이

def solution(todo_list, finished):
    return [work for idx, work in enumerate(todo_list) if not finished[idx]]
