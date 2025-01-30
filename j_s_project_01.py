def main():
    print("Answer 'Yes' or 'No' ")
    safety = input("Would you like to answer a few questions? ")
    if safety.lower() == "yes":
        print("Perfect!!")
    elif safety.lower() == "no":
        print("That's okay, thank you for your time.")
        exit()
    else:
        print("Please only answer 'Yes' or 'No'")
        exit()

    print("I would like to get to know you better.")
    print("It would make me happy if you could answer a few questions")
    name = input("What is your name? ")
    college = input(f"{name}, What is the name of the college that you attend? ")
    highschool = input(f"{name}, What highschool did you attend? ")
    institution1 = input(f"{name}, Which institution comes to mind when you think of fun? ")
    institution2 = input(f"{name}, Which other institution comes to mind? ")
    age = int(input(f"{name}, How old are you? "))
    hobbies = input(f"{name}, What are some of your hobbies? ")
    origin = input(f"{name}, Where are you from? ")
    print("Thank you for telling me about yourself.")
    print()
    print("Correct me if I am wrong.")
    print()
    if institution1.lower() == institution2.lower():
        print(f"You think both {institution1} and {institution2} are equally fun.")
    else:
        more_fun = input(f"{name}, Which institution do you find more fun? {institution1} or {institution2}? ")
        if more_fun.lower() == institution1.lower():
            print(f"I learnt that you think {institution1} is more fun than {institution2}.")
        elif more_fun.lower() == institution2.lower():
            print(f"I learnt that you think {institution2} is more fun than {institution1}.")
        else:
            print("Please input one of the two institutions.")
    print(f"I learnt that your name is {name}.")
    print(f"You are currently a student at {college}.")
    print(f"Your highschool was {highschool}.")
    print(f"You are {age} years old.")
    print(f"You're from {origin}, I heard it's beautiful there.")
    print(f"You like {hobbies}.")
    
    correction = input("Did I get anything wrong? Answer Yes or No. ")
    if correction.lower() == "no":
        print("Wonderful, thank you again for telling me about yourself.")
    elif correction.lower() == "yes":
        corrected = input("Oh no, what did I get wrong? ")
        print(f"{name}: {corrected}")
        print(f"Do forgive me {name}, I will remember that better in the future.")
    else:
        print("What do you mean?")
    

if __name__ == "__main__":
    main()