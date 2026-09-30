def num_input(prompt):
    while True:
        user = input(prompt)
        if user.isdigit() == True:
            return int(user)
        else:
            print("Not a number, try again")


def largest(a, b):
    # Return the larger of two numbers
    pass

def nums(min, max):
    # Print out the numbers between the minimum number and maximum number 
    pass

def is_palindrome(string):
    # Given a string, return True if the string is a palindrome, False otherwise
    pass

def digit_count(string):
    # Given a string, return how many numbers are in the string 
    pass 

def sum(num):
    # Given a number, return the sum of the numbers from 1 up to the number. For example, sum(10) should return 55, since 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55.
    pass

def is_prime(num):
    # Given a number, return True if the number is a prime number or not.
    # We've already done this before, we just need to move it into its own function
    pass

def occurrences(string, character):
    # Given a string and a specific character, count and return how many times that character appears in the string.
    pass

def valid_password(password):
    # Given a password, return True if the password contains an uppercase, lowercase, and a digit. The password must also be longer than 8 characters long. 
    pass


def main():
    while True: 
        print("Enter your choice of a function to test:\n[1] Largest number\n[2] Nums\n[3] Is Palindrome\n[4] Digit Count\n[5] Sum\n[6] Is Prime\n[7] Occurrences\n[8] Valid Password\n[9] to exit")
        choice = num_input(">> ")
        if choice == 1:
            num1 = num_input("Enter your first number: ")
            num2 = num_input("Enter your second number: ")
            print(f"The larger number is {largest(num1, num2)}")
        elif choice == 2:
            min = num_input("Enter your minimum number: ")
            max = num_input("Enter your maximum number: ")
            nums(min, max)
        elif choice == 3:
            text = input("Enter your string: ")
            if is_palindrome(text):
                print(f"{text} is a palindrome")
            else:
                print(f"{text} is not a palindrome")
        elif choice == 4:
            text = input("Enter your string: ")
            print(f"There are {digit_count(text)} digits in {text}")
        elif choice == 5:
            num = num_input("Enter your maximum number to go up to: ")
            print(f"The sum of 1 to {num} is {sum(num)}")
        elif choice == 6:
            num = num_input("Enter a number: ")
            if is_prime(num):
                print(f"{num} is a prime number")
            else:
                print(f"{num} is not a prime number")
        elif choice == 7:
            string = input("Enter a string: ")
            character = input("Enter a single character to check: ")
            print(f"{character} appears in {string} {occurrences(string, character)} times")
        elif choice == 8:
            password = input("Enter a password: ")
            if valid_password(password):
                print(f"{password} is a valid password")
            else:
                print(f"{password} is not a valid password")
        elif choice == 9:
            return


if __name__ == "__main__":
    main()
