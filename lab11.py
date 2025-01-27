def while_loop(num):
    while num > 0:
        print(f"While count: {num}")
        num += -1

def for_loop(num):
    for count in range(num,0,-1):
        print(f"For count: {count}")

def main():
    counter = 10
    while_loop(counter)
    for_loop(counter)

if __name__ == "__main__":
    main()