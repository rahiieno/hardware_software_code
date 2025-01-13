def main():
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

if __name__ == "__main__":
    main()