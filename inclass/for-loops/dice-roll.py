import random

ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0



for count in range (100):
    dice = random.randint(1,6)

    if dice == 1:
        print ("1")
        ones = ones + 1
    elif dice == 2:
        print ("2")
        twos = twos + 1
    elif dice == 3:
        print ("3")
        threes = threes + 1
    elif dice == 4:
        print ("4")
        fours = fours + 1
    elif dice == 5:
        print ("5")
        fives = fives + 1
    else:
        print ("6")
        sixes = sixes + 1
        
print ("You rolled: ")        
print ("1s:", ones)
print ("2s:", twos)
print ("3s:", threes)
print ("4s:", fours)
print ("5s:", fives)
print ("6s:", sixes)
        
