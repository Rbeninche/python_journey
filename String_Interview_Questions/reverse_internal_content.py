s = input("Enter sentence: ")

list_s = s.split()

reverse_list = []

for word in list_s:
    reverse_list.append(word[::-1])

output = ' '.join(reverse_list)

print(output)
