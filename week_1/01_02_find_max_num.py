input = [3, 5, 6, 1, 2, 4]

def find_max_num(array):
    max_num = array[0] # 왜 0번째 원소를 넣어주냐면 배열안의 임의 값을 비교해나가기 때문에
    for num in array:
        if num > max_num: # num이 max_num보다 큰 경우
            max_num = num # max_num을 num으로 교체해라
    return max_num

result = find_max_num(input)
print(result)