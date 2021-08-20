# Facebook 기출문제
input = [0, 3, 5, 6, 1, 2, 4]

# 더하기 또는 곱하기, 곱하기가 더 큰 수가 나오지만 원소에 0, 1을 포함(일종의 함정..)
# 0인 경우에는 곱셈보다 덧셈이 낫고, 1의 경우, 곱셈보다 덧셈이 낫다

def find_max_plus_or_multiply(array):
    multiply_sum = 0 # 변수에 현재 계산 중인 합계를 정의
    for number in array: # 반복시작, 인풋으로 들어온 값들을 하나하나 반복해 변수에 담아준다
        if number <= 1 or multiply_sum <= 1: # 숫자가 1보다 작거나 같거나, multiply_sum이 1보다 작거나 같을 때
            multiply_sum += number # multiply_sum과 number를 더해줘야 한다 <1의 경우, 곱셈보다 덧셈이 낫다>
        else:
            multiply_sum *= number # 그러한 경우가 아니라면 그냥 모두 곱셈을 수행
    return multiply_sum


result = find_max_plus_or_multiply(input)
print(result)