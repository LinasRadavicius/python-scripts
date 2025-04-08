userInput = input("Is it raining outside? (Yes/No): ")
userInput2 = input("Is it cold outside? (Yes/No)")

if userInput == "Yes":
    userInput = True
elif userInput == "No":
    userInput = False
else:
    print("Please type either Yes or No")

if userInput2 == "Yes":
    userInput2 = True
elif userInput2 == "No":
    userInput2 = False
else:
    print("Please type either Yes or No")

if userInput == False and userInput2 == True:
   print("Its cold outside, but not raining. Bring your jacket")
elif userInput == True and userInput2 == False:
    print("It's raining outside, but not cold. Bring your Umbrella")
elif userInput == True and userInput2 == True:
    print("It's both raining and Cold outside. Bring your Umbrella and Jacket")
elif userInput == False and userInput2 == False:
    print("It's neither raining or cold outside. leave your Umbrella and jacket at home")



