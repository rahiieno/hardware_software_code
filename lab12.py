def greeting():
    print("I can only stop if you type exit.")
    print("Do you want me to stop? ")
    print("Type exit then!!")
    return input("Im waiting :)) !!  ").lower().strip()

def main():
    count = 0
    run_loop = greeting()

    while run_loop != "exit":
        run_loop = greeting()

if __name__ == "__main__":
    main()
