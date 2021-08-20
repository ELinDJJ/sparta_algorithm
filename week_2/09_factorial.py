# Factorial(n) = n * Factorial(n - 1)
# ......
# Factorial(1) = 1


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n -1 ) # recursion depth exceeded 리컬젼에러가 발생, 탈출 포인트를 지정해줘야한다


print(factorial(5))