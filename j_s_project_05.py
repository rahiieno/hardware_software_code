def welcome():
    print("This program will add two whole number of your choosing.")
    print("I will continue to ask what whole numbers you would like to add until you say 'exit'.")
    print("You can exit at any time of the code.")

def main():
    welcome()

    while True:
        num1 = input("What is your first number? ").strip()  
        if num1.lower() == 'exit':  
            print("Thank you for using this program.") 
            return
        

        try:
            num1 = int(num1)
            print(f"{num1} is a good number.")
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        num2 = input("What is your second number? ").strip()
        if num2.lower() == 'exit':
            print("Thank you for using this program.")
            return
        

        try:
            num2 = int(num2)
            print(f"{num2} is a good number.")
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        total = num1 + num2
        print("Let's do some adding!!!")
        print(f"{num1} + {num2} = {total}")
        break
    
    while True:
        continue_program = input("Would you like to continue this program? (yes/no) ")
        if continue_program.lower() == "no":
            print("Goodbyeee!!")
            break
        elif continue_program.lower() == "yes":
            print("Continuing program...")
            return main()
        else:
            print("Please only enter yes or no.")


if __name__ == "__main__":
    main()