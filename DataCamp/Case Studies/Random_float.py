
#Randomness has many uses in art, science, statistics, cryptography, gaming, gambling and other fields. 
#Here using the randomness to simulate a game. 

#The functionality I'm using is contained in the "random" package, a sub-package of numpy.
#Import numpy as np 
import numpy as np

#seed() sets the random seed so that the result reproducible between simulations. 
#Set the seed 
np.random.seed(123)

#rand() generates random numbers. If you're not specify input to this method, it will generate random float between zero to one. 
#Generate and print random float
print(np.random.rand())
