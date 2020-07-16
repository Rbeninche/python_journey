s = input("Enter sentence: ")

list_s = s.split()

output = list_s[::-1]

reverse_output = ' '.join(output)

print(reverse_output)
