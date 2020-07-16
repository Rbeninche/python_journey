# Write an application to find the number of each letter in a given string

word = input('Enter any string: ')

d = {}

for ch in word:
    d[ch] = d.get(ch, 0) + 1


for k, v in d.items():
    print(k, 'occurs', v, 'times')
