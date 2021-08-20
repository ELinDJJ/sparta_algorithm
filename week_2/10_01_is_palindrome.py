input = "tomato"

def is_palindrome(string):
    n = len(string)
    for i in range(n):
        # i는 0부터 n-1까지 반복, 문자열의 맨앞 글자와 맨 뒤 글자가 동일한지 비교
        if string[i] != string[n - 1 - i]:
            return False

    return True


print(is_palindrome(input))