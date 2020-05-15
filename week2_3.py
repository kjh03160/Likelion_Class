"""
LCS : 가장 긴 공통의 부분 문자열

두개의 string이 주어졌을 때 공통으로 들어가 있는 가장 긴 부분 문자열 찾기

"""

string1 = 'abcde'
string2 = 'abefg'

matrix = [[0 for i in range(len(string1))] for k in range(len(string2))]

print(string1[4], string2[2])

x = 0
y = 0
val = 0
while x < len(string1):
    y = 0
    while y < len(string2):
        if string1[x] == string2[y]:
            print(x, y)
            val += 1
        matrix[x][y] += val

        y += 1
    x += 1

for i in matrix:
    print(i)





#
#
# for i in range(len(string1)):
#     for k in range(len(string2)):
#         if string1[i] == string2[k]:
#             matrix[i][k] += 1
#         matrix[i][k]