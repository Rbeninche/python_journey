def almost_there(num):
    return (abs(100 - num) <= 10) or (abs(200 - num) <= 10)


result = almost_there(90)

result1 = almost_there(104)

result2 = almost_there(150)

result3 = almost_there(209)

print(result)
print(result1)
print(result2)
print(result3)
