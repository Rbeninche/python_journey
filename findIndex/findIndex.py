s = input("Enter your text here: ")

subs = input("Enter substring to search: ")

index = s.find(subs)

if index == -1:
    print('Specified substring cannot be found')

while index != -1:
    print('{} present at index: {}'.format(subs, index))
    index = s.find(subs, index + len(subs), len(s))

print('Number of occurences is: {}'.format(s.count(subs)))
