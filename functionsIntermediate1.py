import random
def randInt(min=0  , max=100   ):
    if(max>min and max > 0):
        num = int(random.random()*(max-min)+min)
        print("max = " + str(max))
        print("min = " + str(min))
        return num
    else:
        print("Please make sure that max is greater than zero and greater than minimum")
print(randInt(max=-1)) 		
# should print a random integer between 0 to 100
print(randInt(max=50)) 
# should print a random integer between 0 to 50
print(randInt(min=50)) 
# should print a random integer between 50 to 100
print(randInt(min=50, max=500))    
# should print a random integer between 50 and 500
