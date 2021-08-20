input = "소주만병만주소"

# 소주만병만주소
# 주만병만주
# 만병만
# 확인하고자 하는 문자열의 맨앞글자와 맨뒷글자를 확인한 후에는 그 안의 글자들에게만 팰린드롬검사를 하면된다

def is_palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1:-1]) # 주만병만주



print(is_palindrome(input))