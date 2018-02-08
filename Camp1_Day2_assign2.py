import random


def generate_random():
    number = random.randint(1, 10)
    return str(number)


random_number = generate_random()
while True:
    response = input("Guess the number: ")

    if response == random_number:
        print("Correct!")
        break
    else:
        print("Wrong, try again!\n")


