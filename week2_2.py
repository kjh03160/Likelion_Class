"""
ababab -> ab : A -> A4

ababcababc -> ab : A, abc : B -> ABAB

딕셔너리를 어떻게 구성할 것인가?

"""
import string


with open('1.txt', 'r') as file:
    asc = string.ascii_uppercase

    strings = file.read()
    result_dict = {}
    k = 0
    for i in range(0, len(strings), 2):
        val = strings[i: i + 2]
        if val not in result_dict.keys():
            result_dict[val] = asc[k]
            k += 1

    with open('2.txt', 'w') as file2:
        file2.write(str(result_dict))

with open('2.txt', 'r') as file3:
    val = file3. read()
    print(val)


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