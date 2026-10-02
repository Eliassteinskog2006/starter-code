# 1. Print out ut all the numbers between 1 and 30
# 2. If the number is a multiple of 3, instead of printing the number, print out “Fizz”
# 3. If the number is a multiple of 5, instead of printing the number, print out “Buzz”
# 4. If the number is a multiple of 15, instead of printing the number, print out “FizzBuzz”


for count in range (1,31):
    if count % 15 == 0:
        print ("FizzBuzz")
    elif count % 5 == 0:
        print ("Buzz")
    elif count % 3 == 0:
        print ("Fizz")
    else:
        print (count)

