def num_input(prompt):
    while True:
        user = input(prompt)
        if user.isdigit() == True:
            return int(user)
        else:
            print("Not a number, try again")


def largest(a, b):
    if a > b:
        return a
    else:
        return b

def nums(min, max):
    for i in range (min, max + 1):
        print(i)

def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

def digit_count(string):
    count = 0
    for i in string:
        if i.isdigit():
            count += 1
    return count

def sum(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total
    

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def occurrences(string, character):
    count = 0
    for i in string:
        if i == character:
            count += 1
    return count

def valid_password(password):
    upper = False
    lower = False
    digit = False
    for i in password:
        if i.isupper():
            upper = True
        if i.islower():
            lower = True
        if i.isdigit():
            digit = True
            if len(password) > 8 and upper and lower and digit:
                return True
            else:
                return False


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
