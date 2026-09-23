# Lab 3: For Loops Practice

## Instructions

In this lab, we will practice using for-loops and strings. Each problem will require you to consider how to use for-loops to solve the problem. You will need to think about how many times you need to loop, what you need to do each time you loop, and how to use the loop variable to solve the problem. At the beginning, you'll need to ask the user which problem they want to run. You'll then need to use a conditional statement to run the correct problem.

## Problems

1. Write a program that prints out the numbers 1 to 1000. (+5 points)

Challenge: Implement this in three different ways. (+5 points)

2. Write a program that prints out the odd numbers between 1 and 1000. (+5 points)

Challenge: Implement this in three different ways. (+5 points)

3. Write a program that prints out the numbers between 0 and 1000 that are divisible by 3. (+10 points)

Challenge: Implement this without using mod or making the loop step by 3. (+5 points)

4. Write a program that prints out the numbers between 1 and 1000 that are divisible by 3 or 5. (+10 points)

Challenge: Implement this in three different ways (+5 points)

5. Write a program that asks the user to enter a number and prints out all the numbers between 1 and that number that are divisible by 11 or 13. The number entered should be greater than 200. (+10 points) Extra credit if the programs asks again if the number is less than 200. (+5 points)

Challenge: If the user enters a number less than 200, keep asking the user to enter a number until they enter a number greater than 200. (+10 points)

6. Write a program that prints out each letter of a string line by line. String can be entered by the user or a set string. (+5 points)

Challenge: Split the string in half and print out the two halves on two different lines. (+10 points)

7. Write a program that asks the user to enter a string and outputs every second letter. The string must be more than 10 characters long. (+10 points)

Challenge: If the user enters a string shorter than 10 characters long, keep asking the user to enter a string until it is at least 10 characters long. (+10 points)

8. Write a program that rolls 1000 dice and prints out the number that was rolled the most (+15 points). If there's a tie, print out what the tie is (+5 points)

9. Write a program that checks if a given number is a prime number. A prime number is a number that is only divisible by 1 and itself. The user enters a number and the programs prints out whether the number is a prime number or not. (+15 points)

10. Write a program that prints out the prime numbers less than 1000. (+20 points)

## Example Outputs

### Problem 1
  
```bash
1
2
3
4
5
...
999
1000
```

### Problem 2

```bash
1
3
5
7
9
...
997
999
```

### Problem 3

```bash
3
6
9
12
15
...
996
999
```

### Problem 4

```bash
3
5
6
9
12
...
999
1000
```

### Problem 5

```bash
Enter a number greater than 200: 100
Please enter a number greater than 200: 300

11
13
22
26
33
...
297
299
```

### Problem 6

```bash
Enter a string: "Hello world!"

H
e 
l 
l 
o 

w
o 
r 
l 
d 
! 

```

### Problem 7

```bash
Enter a string: Hello World! This is a string 
 
H
l
o
W
r
d
T
i

s
a
s
r
n
```

### Problem 8

```bash
6 was rolled the most at 183 times.
```

### Problem 9
  
```bash
Enter a number: 7
7 is a prime number.

Enter a number: 10
10 is not a prime number.

Enter a number: 41
41 is a prime number.

Enter a number: 1763
1763 is not a prime number.
```

### Problem 10

```bash
2
3
5
7
11
...
991
997
```

## Running the program

To run the program, type the following command in the terminal:

```bash
python3 for_loops.py
```

*Note: If you're using Windows, you may need to use `python` instead of `python3`.*
