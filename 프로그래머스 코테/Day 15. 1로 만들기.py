## 나의 문제풀이

def solution(n):
    answer = 0
    while n != []:
        for i in range(len(n)):
            if n[i] == 1:
                del(n[i])
                break
                
            if n[i] % 2 == 0:
                n[i] = n[i] // 2
            else:
                n[i] = (n[i]-1) // 2
            answer += 1
    return answer # 엄청 어렵게 생각했었네... 이런
  
## 다른사람의 문제풀이              

def solution(num_list):
    answer = 0

    for n in num_list:
        while n != 1:
            n //= 2
            answer += 1

    return answer
