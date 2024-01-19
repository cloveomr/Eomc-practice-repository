## 나의 문제풀이

def solution(myString, pat):
    m, p = myString[::-1], pat[::-1]
    if p in m:
        return myString[:len(m)-m.index(p)]

## 다른사람의 문제풀이

solution=lambda x,y:x[:x.rindex(y)+len(y)] # 무려 문자열의 마지막 인덱스를 찾아주는 rindex()라는 함수가 존재했다...
