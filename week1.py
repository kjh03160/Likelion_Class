"""
1
11
12
1121
122111
112213
k 번째 줄은?

이중 for문, 재귀로 짜보기

"""

def answer(k):
    initial = '1'
    for i in range(k):
        print(initial)

        x = 0
        string = ''
        while x < len(initial):
            std = initial[x]
            count = 1
            while x + 1 < len(initial) and std == initial[x + 1]:
                count += 1
                x += 1
            string += std + str(count)
            x += 1
        initial = string

# answer(10)


def answer_recur(k, boolean=False):
    if boolean:
        return k[0] + str(len(k))
    else:
        x = 0
        indx = [0]
        while x < len(k) - 1:
            if k[x] != k[x + 1]:
                indx.append(x)
            x += 1
        indx.append(len(k))

        string = ''

        length = len(indx)
        i = 0
        start_inx = indx[i]
        while i < length - 1:
            if i + 1 < length:
                end_inx = indx[i + 1]
            else:
                end_inx = indx[-1] + 1

            string += answer_recur(k[start_inx : end_inx + 1], True)
            start_inx = end_inx + 1

            i += 1
        return string


def print_recur(k):
    initial = '1'
    for i in range(k):
        print(initial)
        initial = answer_recur(initial)


print_recur(10)