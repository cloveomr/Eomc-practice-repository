## 나의 문제풀이

def solution(num_list):
    if len(num_list) % 2 == 0:
        hol = sum(num_list[1::2])
        jjak = sum(num_list[0::2])
    else:
        hol = sum(num_list[0::2])
        jjak = sum(num_list[1::2])
    return hol if hol>=jjak else jjak

## 다른사람의 문제풀이

def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2])) # max 함수랑 sum 함수를 잘 사용하여 함수를 간략화 할 수 있었다...
