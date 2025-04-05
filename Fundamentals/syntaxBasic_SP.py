def validate_input(raw_value):
    try:
        val = int(raw_value)
    except ValueError:
        try:
            val = float(raw_value)
        except ValueError:
            print("Please enter a valid number")
            return None
    return val

while True:
    raw = input("Select your number: ")
    userInput = validate_input(raw)
    if userInput is not None:
        break

if userInput > 2:
     print(f"{userInput} is greater than 2")
elif userInput == 2:
    print(f"{userInput} is equal to 2")

else:
    print(f"{userInput} is lower than 2")
