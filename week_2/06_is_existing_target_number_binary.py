finding_target = 39
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
#  업다운게임을 수식으로 구현

#       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# 시도1  최솟값                 시도값                           최대값 -> 업
# 시도2                           최소값       시도값            최대값 -> 업
# 시도3                                          최소값 시도값   최대값 -> 14를 발견!!

def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_max + current_min) // 2
    return False



    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)