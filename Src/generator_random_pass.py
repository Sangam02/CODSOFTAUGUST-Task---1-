import random


# charaters going to use in it

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  

LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
  
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
  
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

passwa = random.choice(DIGITS) + random.choice(LOCASE_CHARACTERS) + random.choice(UPCASE_CHARACTERS) + random.choice(SYMBOLS) + random.choice(DIGITS) + random.choice(LOCASE_CHARACTERS) + random.choice(UPCASE_CHARACTERS) + random.choice(SYMBOLS)
print(passwa)

