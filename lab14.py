def binary_to_decimal(number):
    result = 0
    if len(number) > 0:
        power = len(str(number)) - 1  # Determine the greatest power
        for num in str(number):
            result += int(num) * 2 ** power
            power -= 1 # decrease by 1
    return result

def main():
    num = input("Enter Binary Number: ")
    binary_num = binary_to_decimal(num)
    print(f"Binary {num} to Decimal: {binary_num}")

if __name__ == "__main__":
    main()

