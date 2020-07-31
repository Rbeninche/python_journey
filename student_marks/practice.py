from functools import reduce
from math import *
from random import *
# while True:
#     print('Who are you?')
#     name = input()
#     if name != 'Joe':
#         continue
#     print('Hello, Joe. What is the password? (It is a fish.)')
#     password = input()
#     if password == 'swordfish':
#         break
# print('Access granted.')


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

name = 'Reginald'

print(choice(l))

# total = 1

# for num in l:
#     total *= num

# print(total)

# product = reduce(lambda x, y: x*y, l)

# print(product)

# l2 = []

# count = 0

# while count < len(l):
#     for i in l:
#         if i % 2 == 0 and i != 2:
#             l2.append(i)
#         count = count + 1

# print(l2)

# l2 = [x for x in l if x % 2 == 0 and x != 2]

# print(l2)

# l2 = list(filter(lambda n: n % 2 and n % 3 and n != 7, l))
# print(l2)

# l2 = list(map(lambda n: n*n, l))

# print(l2)


# def summer_69(arr):
#     total = 0
#     add = True
#     for num in arr:
#         while add:
#             if num != 6:
#                 total += num
#                 break
#             else:
#                 add = False
#         while not add:
#             if num != 9:
#                 break
#             else:
#                 add = True
#                 break
#     return total


# # summer_69([1, 3, 5])

# # summer_69([4, 5, 6, 7, 8, 9])

# summer_69([2, 1, 6, 9, 11])


# for i in range(1, 5):
#     print(uniform(5, 10))

# print()

# for i in range(1, 5):
#     print(randrange(0, 101, 10))
