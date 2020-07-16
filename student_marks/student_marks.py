# Write a program to accept student name and marks from the keyboard and creates a dictionary. Also display student marks by taking student name as input

n = int(input('Enter number of students you want to add: '))

d = {}

for i in range(n):
    name = input('Enter student name: ')
    marks = int(input('Enter student marks: '))

    d[name] = marks

print('Student Data Insertion Completed')

print('*' * 30)

print('NAME', '\t\t', 'MARKS')

print('*' * 30)

for k, v in d.items():
    print(k, '\t\t', v)


print('Search operation started.....')

while True:
    name = input('Enter Student name to get marks: ')
    marks = d.get(name, -1)

    if marks == -1:
        print('Student Not Found')

    else:
        print('Marks of', name, 'are:', marks)

    option = input('Do you want to find another student marks(yes/no): ')

    if option.lower() == 'no':
        break

print('Thanks for using our application')
