# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters


def paper_doll(text):
    sentence = ''
    for char in text:
        sentence += char * 3
    return sentence


result = paper_doll('Hello')

print(result)

result1 = paper_doll('Mississippi')

print(result1)
