# src/main.py

def main():
    user_input = input("Enter a command: ")
    if user_input == "exit":
        print("Exiting...")
        return 1
    else:
        print(f"Command received: {user_input}")
        return 0


if __name__ == "__main__":
    result = main()
    if result == 1:
        exit(0)
    else:
        exit(1)
