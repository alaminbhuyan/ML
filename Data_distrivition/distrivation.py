# Create an array containing 250 random floats between 0 and 5
from numpy import *
from matplotlib.pyplot import *
x = random.uniform(0.0,5.0,250)
print(x)
hist(x,5)
show()