# Project 1

Notes Authentication and Setup

## Description

This project is a simple authentication system for a notes application. Users will be asked to login to the system when the program starts. Users will enter their username and password. The program will encrypt the password and compare it to an encrypted password stored on the system.

Upon logging in, the user will be prompted with a menu allowing the user to enter the following commands:

1. `add` - Add a note
2. `remove` - Remove a note
3. `view` - View a note
4. `list` - List all notes
5. `exit` - Exit the program

The user will be prompted to enter a number corresponding to their option. If the user enters an invalid option, the program will print out an error message and continue to ask the user to enter a value until they enter a valid number.

As we haven't talked about certain topics yet, such as storing multiple types of data, this project will not include the core functionality of the notes yet. The idea is to have a working authentication for a user, along with a functional structure setup for the overarching project.

Additionally, you will implement a simple `strong_password` function. This function should take in a password and return `True` if the password satisfies the following requirements:

- Longer than 8 characters long
- Contains at least 1 uppercase character
- Contains at least 1 lowercase character
- Contains at least 1 digit

If any of these are not satisfied, the function should return `False`.

The `strong_password` won't be used yet, but it will come in handy when we eventually create the signup functionality. For now, store the user credentials in the `stored_username` and `stored_password` variables in the `main` function.

If you want to test the `strong_password` function, in the main, you can print out whether a given password is "strong enough" by checking the value returned by the function when the password is provided.

## Topics

- Data Types
- Variables
- Conditional Statements
- Loops
- Functions
- String functions

## Expected Output

```bash

Enter your username: edward
Enter your password: password
Logged in!

Options:
1. Add a new note
2. Remove notes
3. View a note
4. List all notes
5. Exit the program

Enter your choice: 1
Adding a note

Options:
1. Add a new note
2. Remove notes
3. View a note
4. List all notes
5. Exit the program

Enter your choice: 2
Removing a note

Options:
1. Add a new note
2. Remove notes
3. View a note
4. List all notes
5. Exit the program

Enter your choice: 3
Viewing a note

Options:
1. Add a new note
2. Remove notes
3. View a note
4. List all notes
5. Exit the program

Enter your choice: 4
Listing all notes

Options:
1. Add a new note
2. Remove notes
3. View a note
4. List all notes
5. Exit the program

Enter your choice: 5
Exiting the program

```

## Specification

| Grade   | Task    |
|--------------- | --------------- |
| A+   | <ul><li>Everything from A</li><li>If an invalid value is given, a warning message is given.</li><li>Input should not crash the program.</li></ul>   |
| A   | <ul><li>Everything from B</li><li>Strong Password implemented</li><li>Encryption implemented</li></ul>   |
| B   |  <ul><li>Reflection answered completely.</li><li>Options entered by the user prints out the message corresponding to what action will be done later.</li><li>Menu continues to repeat until Option to exit is given.</li></ul>  |
| C  | <ul> <li>Reflection is answered completely.</li> <li> Menu created</li> </ul>|
| D | An attempt was made. Reflection was approached. |
| F | No attempt made. |


