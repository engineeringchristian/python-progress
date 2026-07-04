secret_number=7
while True:
    try:
        user_input = int(input("Guess the secret number!>>"))
        if user_input == secret_number:
            print("Not so secret anymore...")
            break
        else:
            print("Try again!")
    except ValueError:
        print("That isn't a number!")
print("Don't tell anyone!")
