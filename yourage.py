while True: 
    age = input("Enter your age: ")
    
    try:
        age = int(age)
        if age < 0: 
            print("Age can't be negative")
        else:
            break
    except ValueError:
        print("Invalid input")

print(f"You are {age} years old")
