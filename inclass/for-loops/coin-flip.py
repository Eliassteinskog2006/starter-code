import random

heads = 0
tails = 0


for count in range (100):
    coin = random.randint(1,2)

    if coin == 1:
        print ("heads")
        heads = heads + 1
    else:
        print ("tails")
        tails = tails + 1
        
print ("heads:", heads)
print ("tails:", tails)
        
