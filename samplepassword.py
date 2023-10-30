

import random




def generatePassword(n):
   
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIWXYZ123456789!@#$%^&*()"

    """
    The random.sample() method returns a list, so we need to convert it into a string before returning it.
    """

    chosenLetter = random.sample(characters, n)

  
    password = "".join(chosenLetter)

    return password


if __name__ == "__main__":
    n = 12
    password = generatePassword(n)
    print("A randomly selected password is:", password)
