## 나의 문제풀이

def solution(num_list):
    ans = 1
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        for i in num_list:
            ans *= i
        return ans

## 다른사람의 문제풀이

def solution(num_list):
    if len(num_list) >= 11:
        return eval('+'.join(list(map(str, num_list))))
    else:
        return eval('*'.join(list(map(str, num_list)))) # eval 함수를 쓰면 엄청 간단하게 풀 수 있다!!
