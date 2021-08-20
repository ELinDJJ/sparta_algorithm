input = [3, 5, 6, 1, 2, 4]

def is_number_exist(number, array):
    for element in array: # array의 길이만큼 연산 실행
        if number == element: # 비교 연산
            return True
    return False # N * 1 만큼의 시간복잡도

# 하지만 3이 가장 앞에 위치해있어 연산을 실행하자마자 3을 찾아내기 때문에, 원소의 위치가 바뀌면 시간복잡도가 변할 가능성이 있다

result = is_number_exist(3, input)
print(result)


'''def is_number_exist(number, array):
    for element in array:
        if number == element:
            return True
    return False

result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3,[3,5,6,1,2,4]))
print("정답 = Flase 현재 풀이 값 =", result(7,[6,6,6]))
print("정답 = True 현재 풀이 값 =", result(2,[6,9,2,7,1888]))'''