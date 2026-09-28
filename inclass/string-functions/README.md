# String Functions In Class

Today in class, we will write some code that will use string functions to help us understand strings better.

## Digit Check

In the digit-check.py file, ask the user to enter a number. Before casting the number into an integer (and potentially crashing our code), let's check if the value entered contains only digits or if it also contains non-digit characters. If the whole string contains a non-digit character, update a boolean to inform the program that we have a non-numeric value. At the end, print out a message if the entered string contains a non-numeric value. Ask the user to enter the number again if this is the case. However, if the user successfully enters in a purely numeric value, convert that into a number and don't ask the user to continue. 

### Example

```bash
Enter a number: 19k
19k contains a non-numeric value!
Enter a number: 19
19 is a valid number.
```

## Caesar Cipher 

In the caesar-cipher.py file, we will write a simple program to implement a caesar shift. A Caesar shift takes a character and shifts it by some value alphabetically. To learn more, you can look at [https://en.wikipedia.org/wiki/Caesar_cipher](https://en.wikipedia.org/wiki/Caesar_cipher) and check out more information about the caesar cipher. 

In our program, we will ask the user to enter a string and shift each character over by some amount. For now, we will use a shift of 2, but we can always try it with a larger shift and see what happens. To do this, we will use the [ASCII Table](https://asciitable.com/) and refer to the ASCII value of each character.

### Hint 

- Use `ord` and `chr` to convert to its ASCII numeric values and convert it back to its character representation.

### Example 

```bash 
Enter a string: password 

You entered "password" which was shifted into "qbttxpse" with a shift value of 1
```

