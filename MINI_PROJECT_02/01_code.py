history_file = "history.txt" 

def show_history():
    with open(history_file, "r") as f:
        lines = f.readlines()
    if len(lines) == 0:
        print("No history found\n")
    else:
        for line in reversed(lines):
            print(line.strip())

def clear_history():
    open(history_file, "w").close()   # clears file
    print("History cleared\n")

def save_history(ques, reslt):
    with open(history_file, "a") as f:
        f.write(str(ques) + " = " + str(reslt) + "\n")

def calc(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input! Use format: number operator number (e.g., 5 + 3)\n")
        return

    num1 = float(parts[0])
    sign = parts[1]
    num2 = float(parts[2])

    if sign == "+":
        result = num1 + num2
    elif sign == "-":
        result = num1 - num2
    elif sign == "*":
        result = num1 * num2
    elif sign == "/":
        if num2 == 0:
            print("Error: Division by zero!\n")
            return
        else:
            result = num1 / num2
    else:
        print("Invalid operator!\n")
        return

    print(f"RESULT: {result}")
    save_history(user_input, result)

def main():
    print("-- SIMPLE CALCULATOR (type history, clear, or exit) --\n")
    while True:
        user_input = input("Enter calculation or command: ").strip().lower()

        if user_input == "exit":
            print("Goodbye!\n")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calc(user_input)

main()
