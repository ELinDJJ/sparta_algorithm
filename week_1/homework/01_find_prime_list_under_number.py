'''# 1차
input = 20

def find_prime_list_under_number(number):
    prime_list = [] # 소수들을 담을 객체를 생성
    for n in range(2, number + 1): # 2부터 n+1까지 반복하여 확인
        for i in prime_list:
            if n % i ==0: # n을 소수로 나눠서 0이 된다면
                break
        else:
            prime_list.append(n)

    return prime_list

result = find_prime_list_under_number(input)
print(result)'''

# 2차
input = 20

def find_prime_list_under_number(number):
    prime_list = []

    for n in range(2, number + 1):
        for i in prime_list:
            if n % i == 0 and i * i <= n: # 소수의 특성을 환기
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)