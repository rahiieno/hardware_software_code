def main():
    print("Answer 'Yes' or 'No' ")
    safety = input("Would you like to answer a few questions? ")
    if safety == "Yes":
        print("Perfect!!")
    elif safety == "No":
        print("That's okay, thank you for your time.")
    else:
        print("Please only answer 'Yes' or 'No'")

    print("I would like to get to know you better.")
    print("It would make me happy if you could answer a few questions")
    name = input("What is your name? ")
    college = input(f"{name}, What is the name of the college that you attend? ")
    highschool = input(f"{name}, What highschool did you attend? ")
    institution = input(f"{name}, What institution do you think is most fun? ")
    print("Thank you for telling me about yourself.")
    print()
    print("Correct me if I am wrong.")
    print()
    print(f"Your name is {name}.")
    print(f"You are a student at {college}.")
    print(f"You were a student at {highschool}")
    print(f"You find {institution} more fun.")
    correction = input("Did I get anything wrong? Answer Yes or No. ")
    if correction == "No":
        print("Wonderful, thank you again for telling me about yourself.")
    elif correction == "Yes":
        corrected = input("Oh No, What did I get wrong? ")
        print(f"{name}: {corrected}")
        print(f"Do forgive me {name}, I will remember that better in the future.")
    else:
        print("What do you mean?")
    

if __name__ == "__main__":
    main()