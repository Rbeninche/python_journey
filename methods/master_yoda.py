# MASTER YODA: Given a sentence, return a sentence with the words reversed


def master_yoda(str):

    str_list = str.split()

    list_reverse = str_list[::-1]

    list_reverse_str = ' '.join(list_reverse)
    return list_reverse_str


result = master_yoda('I am home')

print(result)

result2 = master_yoda('We are ready')

print(result2)
