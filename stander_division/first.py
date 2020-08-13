from numpy import *
# stander division
speed = [86,87,88,86,87,85,86]
x = std(speed)
print(x)
# find the variance
speed2 = [32,111,138,28,59,77,97]
y = var(speed2)
print(y)
z = std(speed2)
print(z)

# find the percentile
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
a = percentile(ages,60)
print(a)