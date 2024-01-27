## 나의 문제풀이

def solution(arr):
    stk = []
    for i in range(len(arr)):
        if stk == []:
            stk.append(arr[i])
        elif stk[-1] == arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])
    if stk == []:
        return [-1]
    else:
        return stk
        
## 다른사람의 문제풀이

def solution(arr):
    stk = []
    for i in range(len(arr)):
        if stk and stk[-1] == arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])

    return stk or [-1] # return을 이렇게 간략화 할 수도 있다!
