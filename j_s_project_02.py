def welcome():
    print("Welcome to my questioning program.")
    print("I am going to keep asking you questions till you say 'exit'.")

def asking_questions():
    count = 0
    name = input("What is your name? ").strip()
    if 'exit' in name.lower():
        return count, name
    
    while True:
        question_2 = input(f"Where are you from, {name}? ").strip()
        if 'exit' in question_2.lower():
            break
        count += 1

        question_3 = input(f"What college do you attend, {name}? ").strip()
        if 'exit' in question_3.lower():
            break
        count += 1

        question_4 = input(f"What highschool did you attend, {name}? ")
        if 'exit' in question_4.lower():
            break
        count += 1

        question_5 = input(f"What institution is more fun, {name}? ")
        if 'exit' in question_5.lower():
            break
        count += 1

    return count, name

def closing_statement(count,name):
    print(f"\nThank you for answering my questions, {name}.")
    print(f"You answered {count} questions.")

def main():
    welcome()
    count, name = asking_questions()
    closing_statement(count, name)

if __name__ == "__main__":
    main()

    






