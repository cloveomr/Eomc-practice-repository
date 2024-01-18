## 나의 문제풀이

def solution(my_string, alp):
    if alp in my_string:
        return my_string.replace(alp, alp.upper())
    else:
        return my_string ## 나는 if 문을 사용했지만 사용하지 않아도 괜찮았다!!
