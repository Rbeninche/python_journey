s1 = input("Enter first sentence: ")
s2 = input("Enter second sentence: ")

i, j = 0, 0

output = ''

while i < len(s1) or j < len(s2):

    if i < len(s1):
        output = output + s1[i]
    if i < len(s2):
        output = output + s2[i]

    i += 1
    j += 1

print(output)
