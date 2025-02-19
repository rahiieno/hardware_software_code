def welcome(): # Defined a function called welcome that will run print statements.
    print("This program will turn binary to decimal and decimal to binary.")
    print("This program will convet: ") 
    print("1. Binary To Decimal") 
    print("2. Decimal To Binary") 
    print("You can keep converting until you decide to exit.\n")

def binary_to_decimal(binary_str): 
    if not binary_str or not all(char in '01' for char in binary_str):
        return "Invalid binary number. Please only enter 0s and 1s."

    decimal_value = 0
    for i, digit in enumerate(reversed(binary_str)):
        decimal_value += int(digit) * (2 ** i)

    return decimal_value

def decimal_to_binary(decimal_str):
    
    if not decimal_str.isdigit():
        return "Invalid decimal number. Please enter a positive integer."
    
    decimal_value = int(decimal_str)
    return bin(decimal_value)[2:]

def main():
    welcome()


    while True:
        print("\nWhich would you like to convert?")
        print(" 1. Binary To Decimal")
        print(" 2. Decimal To Binary")
        print(" 3. Exit")

        choice = input("What is your decision? ").strip()

        if choice == "1":
            print("Converting Binary to Decimal.")
            print("'0' and '1' are valid numbers.")
            binary_input = input("Enter a binary number: ").strip()
            result = binary_to_decimal(binary_input)
            print(f"Conversion: {result}")

        elif choice == "2":
            print("COnverting Decimal To Binary.")
            decimal_input = input("Enter a decimal number: ").strip()
            result = decimal_to_binary(decimal_input)
            print(f"Conversion: {result}")

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please only enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

    