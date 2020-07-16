
def spy_game(nums):

    code = [0, 0, 7, 'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)   # code.remove(num) also works

    return len(code) == 1


result1 = spy_game([1, 2, 4, 0, 0, 7, 5])  # True
result2 = spy_game([1, 0, 2, 4, 0, 5, 7])  # True
result3 = spy_game([1, 7, 2, 0, 4, 5, 0])  # False

print(result1)
print(result2)

print(result3)
