# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name


def old_macdonald(str):

    slice_first_to_third = str[:3].capitalize()
    slice_fourth_to_rest = str[3:].capitalize()

    capitalize_first_and_fourth = slice_first_to_third + slice_fourth_to_rest

    return capitalize_first_and_fourth


result = old_macdonald('macdonald')

print(result)
