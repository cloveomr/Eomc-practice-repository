## 나의 문제풀이

def solution(my_string, is_prefix):
    if my_string[:len(is_prefix)]==is_prefix: return 1
    return 0

## 9, 접미사인지 확인하기 코드에서 약간 수정함
## 파이썬 라이브러리 startswith를 쓰면 더 쉽게 풀 수 있었다...!!
