input = "hello my name is sparta"

def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0 # 가장 많이 발생했던 빈도수를 저장하는 변수
    max_alphabet_index = 0 # 가장 많이 나왔던 알파벳의 인덱스를 저장하는 변수
    for index in range(len(alphabet_occurrence_array)): # for문을 돌면서 하나하나 비교
        # index 0 -> alphabet_occurrence 3
        alphabet_occurrence = alphabet_occurrence_array[index]

    if alphabet_occurrence > max_occurrence:
        max_occurrence = alphabet_occurrence
        max_alphabet_index = index
    return chr(max_alphabet_index + ord('a'))
    result = find_max_occurred_alphabet
   # print(max_alphabet_index)인 경우, 출력은 0, a가 가장 많이 출현하였으르모 index인 0이 출력

    return alphabet_occurrence_array
'''
How to get the ASCII value of a character
https://stackoverflow.com/questions/227459/how-to-get-the-ascii-value-of-a-character
a-> 0
a -> ord(a) -> 97 -ord(a) = 0

0 -> a
0 -> 0 + ord(a) -> 97 -> chr(97) -> a'''

result = find_max_occurred_alphabet(input)
print(result)
