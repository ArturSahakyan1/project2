
import random
import string



def gp(length=1):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) 
    for i in range(length))
    return password



if __name__ == "__main__":
    length = int(input("length: "))

    password = gp(length)
    print(" Password is following:", password)

