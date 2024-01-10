## 나의 문제풀이

def solution(n, slicer, num_list):
    if n == 1:
        return num_list[0:slicer[1]+1]
    if n == 2:
        return num_list[slicer[0]:]
    if n == 3:
        return num_list[slicer[0]:slicer[1]+1]
    if n == 4:
        return num_list[slicer[0]:slicer[1]+1:slicer[2]]

## 다른사람의 문제풀이

def solution(n, slicer, num_list):
    a, b, c = slicer ## 리스트 원소를 각각의 변수에 저장할 수 있다.
    return [num_list[:b + 1], num_list[a:], num_list[a:b + 1], num_list[a:b + 1:c]][n - 1]

