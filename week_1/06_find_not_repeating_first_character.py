
# 반복되지 않는 문자를 찾을려면 문자들이 카운트되서 어떻게 저장되는지 생각해봐야한다
# 최빈값구하는 방법 활용
input = "abadabac"
def find_not_repeating_first_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))

    for char in string:
        if char in not_repeating_character_array:
            return char
# 입력된 문자열 내에서 반복되지 않는 첫번째 문자를 찾아서 반환해줘야 하기 때문에 string 을 다시 반복해서 돌면서 첫 번째 반복되지 않는 문자를 찾아 반환
    return "_"

result = find_not_repeating_first_character(input)
print(result)




'''not_repeating_character_array = [] # 반복되지 않는 문자를 이 변수에 넣어준다
    for index in range(len(alphabet_occurrence_array)): # 알파벳의 길이만큼 반복해준다
        alphabet_occurrence = alphabet_occurrence_array[index] # 각 문자의 빈도수가 저장된다
        if alphabet_occurrence == 1: # 만약 출현이 1이면
            not_repeating_character_array.append(chr(index + ord("a"))) # not_repeating_character_array에 담아라
    print(not_repeating_character_array)
    return "_"

#result = find_not_repeating_first_character
#print(not_repeating_character_array)
#print(result)'''

