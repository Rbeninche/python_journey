# Write a program to generate a random password of 6 length where 1,3,5 characters are alphabet symbols and 2,4,6 are digits
from random import *

import string

# alphabets = 'ABCDEGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

alphabet_string = string.ascii_lowercase + string.ascii_uppercase
alphabets = list(alphabet_string)

print(choice(alphabets), choice(digits), choice(alphabets),
      choice(digits), choice(alphabets), choice(digits), sep='')

# Print alphabet or digits at any position

otp = ''

for i in range(6):
    otp += str(choice(alphabets + list(digits)))

print(otp)
