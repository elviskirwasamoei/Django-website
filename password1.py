import random

def generatePassword(n):
    
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    
    chosenLetter = random.sample(characters, n)
    password = "".join(chosenLetter)
    return password
if __name__ == "__main__":
     n = int(input("Enter the length of the password: "))
     
     password = generatePassword(n)
     print("A randomly selected password is:", password)