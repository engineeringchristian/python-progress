import random as r

randint1 = r.randint(-10000, 10000)
randint2 = r.randint(-10000, 10000)

a = min(randint1, randint2)
b = max(randint1, randint2)
secret_number = 7
while secret_number == 7:
    secret_number = r.randint(a, b)

attempts = 0

while True:

    user_input = input("Guess the secret number: ")

    try:
        user_input = int(user_input)
        attempts += 1
    except ValueError:
        print("Invalid input")
        continue
    if user_input == secret_number:
        print(f"That used to be the secret number. It took you {attempts} attempts.")
        exit()
    elif user_input == 7:
        print("That is the lucky number")
    elif user_input < secret_number:
        print("That is too low.")
    elif user_input > secret_number:
        print("That is too high.")
