import random as rnd
import string

class PasswordGenerator():
    def __init__(self, countOfNumbers = 8):
        self._countOfNumbers = countOfNumbers
    
    def generatePassword(self):
        password = ''
        allowedSymbol = list()
        lowerChars = string.ascii_lowercase
        upperChars = string.ascii_uppercase

        # sequence of chars
        for i in lowerChars:
            allowedSymbol += str(i)

        for i in upperChars:
            allowedSymbol += str(i)

        # sequence of int
        for i in list(range(10)):
            allowedSymbol += str(i)

        # add more symbols
        allowedSymbol += ['*', '-', '_', '(', ')', '^', '%', '$', '#', '@'] * 2   
    
        for i in range(self._countOfNumbers):
            char = rnd.choice(allowedSymbol)
            password += char
            
        return password
    
PG = PasswordGenerator()

PG._countOfNumbers = int(input("Please input password length: "))

print(PG.generatePassword())