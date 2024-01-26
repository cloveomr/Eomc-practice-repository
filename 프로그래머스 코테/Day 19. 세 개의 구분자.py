## 나의 문제풀이

def solution(myStr):
    for i in myStr:
        if i == "a" or i == 'b' or i == 'c':
            myStr = myStr.replace(i, " ")
    if myStr.split() == []:
        return ["EMPTY"]
    else:
        return myStr.split()

## 다른사람의 문제풀이

def solution(myStr):
    answer = [x for x in myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split() if x] ## replace 함수 중복이 가능하다!!
    return answer if answer else ['EMPTY']
