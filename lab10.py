def main():
    print("This program adds two numbers under 1000.")
    print("I will continue to ask what numbers you would like to add until you say 'exit'. ")

    while True:
        num1 = input("What number would you like to add? ")
        if num1.lower() == "exit":
            print("Alrightyy!!")
            break
        
        num2 = input("What number would you like to add? ")
        if num1.lower() == "exit":
            print("Alrightyy!!")
            break

        try:
            num1 = int(num1)
            num2 = int(num2)
        except ValueError:
            print("Enter a valid number. ")
            continue

        if num1 > 999 or num2 > 999:
            print("Number too big.")
            continue

        total = num1 + num2
        print(f"{num1} + {num2} = {total}")


if __name__ == "__main__":
    main()
