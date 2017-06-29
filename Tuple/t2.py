# -*- coding: UTF-8 -*-
import random

print random.choice( [1,2,3,4,5,6,7,8,9,10]  )


print random.randrange(100, 1000, 2)


print random.random()

list = [20, 16, 10, 5];
random.shuffle(list)
print list
print random.uniform(1, 2) 
random.seed( 10 )

print random.random()
random.seed( 10 )

print random.random()

random.seed( 10 )

print random.random()


