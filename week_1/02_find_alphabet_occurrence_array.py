'''
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
            # a를 0으로, b를 1로, c를 2로 어떻게 변환할 것인가
        arr_index = ord(char) - ord("a") # char-97(a) = 배열의 인덱스값이 되도록 지정한 뒤, 변수로 저장
        alphabet_occurrence_array[arr_index] += 1 # alphabet_occurrence_array[arr_index]의 인덱스값을 하나씩 증가시키기

    return alphabet_occurrence_array

print(find_alphabet_occurrence_array("Hello my name is sparta"))
'''


def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array
print(find_alphabet_occurrence_array("Hello my name is sparta"))