"""
파일 입출력으로 입력 받아서 읽어서 해당 문자열이 몇개 연속인지? -> 후 파일 저장
"""

def answer(file_name):
    result = []
    with open(file_name + '.txt', 'r', encoding='UTF-8') as file:
        with open('result.txt', 'w', encoding='UTF-8') as result_f:
            lines = file.read().split('\n')

            for line in lines:
                string = ''
                k = 0
                while k < len(line):
                    std = line[k]
                    count = 1
                    while k + 1 < len(line) and std == line[k + 1]:
                        count += 1
                        k += 1
                    string += std + str(count)
                    k += 1
                result_f.write(string + '\n')
                result.append(string)

    return result

print(answer('1'))