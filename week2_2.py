"""
ababab -> ab : A -> A4

ababcababc -> ab : A, abc : B -> ABAB

딕셔너리를 어떻게 구성할 것인가?

"""
import string


with open('LCS_text.txt', 'r+') as file:
    asc = string.ascii_uppercase

    strings = file.read()
    result_dict = {}
    k = 0

    with open('LCS_result.txt', 'w') as file2:
        for i in range(0, len(strings), 2):
            val = strings[i: i + 2]
            if val not in result_dict.keys():
                result_dict[val] = asc[k]
                file2.write(asc[k])
                k += 1

    with open('LCS_dict.txt', 'w') as file3:
        for key, val in result_dict.items():
            file3.write(key + ":" + val + '\n')


with open('LCS_dict.txt', 'r') as file4:
    str_dict = {}
    dict_list = file4.readlines()
    for i in dict_list:
        line = i.split(':')
        str_dict[line[1].strip()] = line[0]

    with open('LCS_result.txt', 'r') as file5:
        text = file5.read()
        result = ''
        for i in text:
            result += str_dict[i]

        print(result)





# strings = "ababcababc"
# asc = string.ascii_uppercase
#
# result_dict = {}
# k = 0
# result_string = ''
# for i in range(0, len(strings), 2):
#     val = strings[i : i + 2]
#     if val not in result_dict.keys():
#         result_dict[val] = asc[k]
#         k += 1
#     # result_string += result_dict[val]
#
# for i in range(0, len(strings), 2):
#     val = strings[i : i + 2]
#     result_string += result_dict[val]
#
# print(result_dict, result_string)