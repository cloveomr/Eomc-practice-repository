## 나의 문제풀이

def solution(date1, date2):
    date1, date2 = list(map(str,date1)), list(map(str,date2))
    if int("".join(date1)) < int("".join(date2)):
        return 1
    else:
        return 0
