import random
import time

HACKTOBERFEST = 100

def hacktoberfest():
    i = random.randint(1,5)
    print("The hacktoberfest number is...", i)
    return i


def HACKtoberFEST():
    print("Hello, World!")
def HackToBerFest():
    print('Hello, Opensource!')


while HACKTOBERFEST == 100:
    time.sleep(1)

    if hacktoberfest() >= 3:
        HACKtoberFEST()
        break
    elif hacktoberfest()<3:
        HackToBerFest()
        break
        
