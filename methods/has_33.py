# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere


def has_33(myList):

    for i in range(0, len(myList) - 1):
        if myList[i] == 3 and myList[i+1] == 3:
            return True
    return False


def has_33(myList):

    for i in range(0, len(myList) - 1):
        if myList[i:i+2] == [3, 3]:
            return True
    return False


result = has_33([1, 3, 3])
result1 = has_33([1, 3, 1, 3])
result2 = has_33([3, 1, 3])

print(result)
print(result1)
print(result2)
