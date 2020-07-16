# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False


def makes_twenty(a, b):

    total = a + b
    if total == 20 or a == 20 or b == 20:
        return True
    else:
        return False


result = makes_twenty(10, 20)

result1 = makes_twenty(12, 8)

result2 = makes_twenty(2, 3)

print(result)
print(result1)
print(result2)
