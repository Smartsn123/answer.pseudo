#import random library from python
from random import choice

#function parameter is assumed to be string
#assuming we want random number generated to be between 6 and 15( not including)
def generateRandom(name):
     return name+str(choice( range(7,15) )) 


#if the current script is executed by compiler
#then this condition stands true
if __name__ == "__main__":
	print "Enter your name"
	print generateRandom(raw_input())