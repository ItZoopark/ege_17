# with open("17.txt") as fin:
#     list = []
#     lines = tuple(open(fin, 'r'))
#     print(lines)

# lines = list(open("17-202.txt", 'r'))
# list = [int(el[:-1]) for el in lines]
# print(list)
# count = 0
# maximum = -30001
# for i in range(1, len(list) - 1):
#     if list[i + 1] > 0 and 99 < list[i + 1] < 1000 and list[i + 1] % 100 == 12 and \
#             not(list[i] > 0 and 99 < list[i] < 1000 and list[i] % 100 == 12) and \
#             not (list[i+2] > 0 and 99 < list[i+2] < 1000 and list[i+2] % 100 == 12):
#         count += 1
#         maximum = max(list[i] + list[i + 1] + list[i + 2], maximum)
#     # if list[i] % 3 == 0 or list[i + 1] % 3 == 0:
#     #     count += 1
#     #     maximum = max(list[i] + list[i+1], maximum)
#
# print(count)
# print(maximum)
# ---------------------------------
# 4407 Поляков Генератор Вариантов
# ---------------------------------
# lines = list(open("17.txt", 'r'))
# #
# list = [int(el[:-1]) for el in lines]
#
# count = 0
# maximum = -20001
# for i in range(len(list) - 1):
#     if list[i] % 3 == 0 or list[i + 1] % 3 == 0:
#         count += 1
#         maximum = max(list[i] + list[i + 1], maximum)
#
# print(count)
# print(maximum)
# -------------------------------
# 2331
# def toBase(x, base):
#     res = ''
#     change = False
#     while x != 0:
#         if x % base > 9:
#             change = True
#         res += str(x % base)
#         x //= base
#     return (res[::-1], change)
#
#
# def task2331(N):
#     tuple_res = toBase(338, N)
#     if not tuple_res[1]:
#         res = tuple_res[0]
#         if len(res) == 3 and res[-1] == '2':
#             return True
#         else:
#             return False
#     else:
#         return False
#
#
# for N in range(10000, 1, -1):
#     if task2331(N):
#         print(N)
#         break
# -------------------------------------------
# 4721
# input = list(map(int, open('4721.txt').read().splitlines()))
# suma = 0
# for x in input:
#     if x % 61 == 0:
#         while x != 0:
#             suma += x % 10
#             x //= 10
#
# min_sum = 20001
# count = 0
# for i in range(len(input) - 1):
#     a = input[i]
#     b = input[i + 1]
#     if a > suma >= b and b % 100 == 33 or b > suma >= a and a % 100 == 33:
#         min_sum = min(min_sum, a+b)
#         count += 1
# print(min_sum, count)


# input = list(map(int, input))
# print(input)

def isAr(x):
    if x[2] - x[1] == x[1] - x[0] and x[2] > x[0]:
        return x[2] - x[1]
    else:
        return 0


def isGe(x):
    if x[2] / x[1] == x[1] / x[0] and x[2] > x[0]:
        return x[2] / x[1]
    else:
        return 0


def pol_5022():
    count = 0
    max_six = 0
    data = list(map(int, open('17-281.txt').read().splitlines()))
    for i in range(len(data) - 5):
        if isAr(data[i:i + 3]) and isGe(data[i + 3:i + 6]) or isGe(data[i:i + 3]) and isAr(data[i + 3:i + 6]):
            if isAr(data[i:i + 3]) == isGe(data[i + 3:i + 6]) or isGe(data[i:i + 3]) == isAr(data[i + 3:i + 6]):
                count += 1
                max_six = max(sum(data[i:i + 6]), max_six)
    print(count, max_six)


# pol_5022()

def pol_4319():
    data = list(map(int, open('17-4.txt').read().splitlines()))
    count_all = 0
    max_x = 0
    min_x = 10001
    for x in data:
        count = 0
        if x % 2 == 0: count += 1
        if x % 3 == 0: count += 1
        if x % 5 == 0: count += 1
        if x % 7 == 0: count += 1
        if count == 2:
            count_all += 1
            max_x = max(x, max_x)
            min_x = min(x, min_x)
    print(count_all, max_x + min_x)

pol_4319()
