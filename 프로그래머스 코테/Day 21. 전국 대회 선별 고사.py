## 나의 문제풀이

def solution(r, a):
    answer = {}
    for i in range(len(a)):
        if a[i] == True:
            answer[i] = r[i]
    dic = sorted(answer,key=lambda x:answer[x])
    return 10000 * dic[0] + 100 * dic[1] + dic[2]

## 다른 사람의 문제풀이

def solution(rank, attendance):
    arr = sorted([(x, i) for i, x in enumerate(rank) if attendance[i]])
    return arr[0][1] * 10000 + arr[1][1] * 100 + arr[2][1]
