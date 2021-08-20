input = "011110"

# 규칙성
# 1 문자열이 뒤집어질 , 0에서 1, 1에서 1이 될 때
# 2 첫 번 째 원소가 1인지 0인지에 따라서 숫자를 추가

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == '0': # 만약 스트링의 첫 숫자가 0이라면
        count_to_all_one += 1
    elif string[0] == '1': # 그렇지 않고 스트링의 첫 숫자가 1이라면
        count_to_all_zero += 1

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]: # 1에서 0, 또는 0에서 1이 되었다는 의미
            # 스트링 i가 [i+1]와 같지 않으면(그 다음자리의 숫자와 같지 않으면) 00이 아닌 01일 때?
            if string[i + 1] == '0': # [i+1]가 0이면
                count_to_all_one += 1 # count_to_all_one이 하나씩 증가 - 1에서 0이 되었다면 앞의 수를 모두 0을로 변환
            if string[i + 1] == '1': # [i+1]가 1이면
                count_to_all_zero += 1 # count_to_all_zero 증가
    print(count_to_all_zero, count_to_all_zero)

    return 1


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
