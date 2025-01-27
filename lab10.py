def main():
    print("This program adds two numbers.")

    num1 = input("What number would you like to add? ")
    num2 = input("What other number would you like to add? ")
    
    total = int(num1) + int(num2)

    print(f"{num1} + {num2} = {total}")


if __name__ == "__main__":
    main()