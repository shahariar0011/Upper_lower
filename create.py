def main():
    print("Welcome to my site.")
    print("Please select your Topic.")
    print("1. Uppercase")
    print("2. Lowercase")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        word = input("Enter a word to convert to Uppercase: ")
        print("Output: ", word.upper())
    elif choice == '2':
        word = input("Enter a word to convert to Lowercase: ")
        print("Output: ", word.lower())
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
