# Program to reverse string

# 1) Slice operator

s = input("Enter your string: ")

output = s[::-1]

print(output)

# 2) Reverse function

s = input("Enter your string: ")

output = reversed(s)

r = ''.join(output)
print(r)

# 3) Using While loop

s = input("Enter your string: ")
output = ''
i = len(s) - 1

while i >= 0:
    output += s[i]
    i -= 1

print(output)
