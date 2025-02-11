import random as r1

def generate_random():
    return r1.randint(1,10)

def check_number(number_str):
    valid_number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    if number_str in valid_number:
        return number_str
    else:
        return check_number(input("Invalid Number, Try again!!! "))
       
def main():
    random_number = generate_random()
    choice = input("Please enter a number between 1-10: ")
    choice = check_number(choice)
    if int(choice) != int(random_number):
        print("Better luck next time..")
        print(f"You should have guessed {random_number}")
    else:
        print("You are a winner!!")
        print(f"The winning guess was {random_number}")


if __name__ == "__main__":
    main()
