## 나의 문제풀이

def solution(arr1, arr2):
    if len(arr1) < len(arr2):
        return -1
    elif len(arr1) > len(arr2): # 이 부분을 더 짧게 할 수 있었는데 살짝 아쉽
        return 1
    else:
        if sum(arr1) < sum(arr2):
            return -1
        elif sum(arr1) > sum(arr2):
            return 1
        else:
            return 0
