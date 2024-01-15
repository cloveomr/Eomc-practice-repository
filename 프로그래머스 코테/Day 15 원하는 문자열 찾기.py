## 나의 문제풀이

def solution(myString, pat):
    myString, pat = myString.lower(), pat.lower()
    if pat in myString:
        return 1
    else:
        return 0


## 다른사람의 문제풀이

def solution(myString, pat):
    return int(pat.lower() in myString.lower()) ## boolean을 int화 한다음 return
