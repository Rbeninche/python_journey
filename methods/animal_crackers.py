# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter


def animal_crackers(str):
    index_of_space = str.index(' ')
    if str[0] == str[index_of_space + 1]:
        return True
    else:
        return False


result = animal_crackers('Levelheaded Llama')

print(result)
result = animal_crackers('Crazy Kangaroo')

print(result)
