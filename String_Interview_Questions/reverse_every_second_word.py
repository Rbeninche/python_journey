s = input("Enter sentence: ")

s_list = s.split()

i = 0

l1 = []

while i < len(s_list):
    if i % 2 == 0:
        l1.append(s_list[i])

    else:
        l1.append(s_list[i][::-1])

    i += 1

output = ' '.join(l1)
print(output)
