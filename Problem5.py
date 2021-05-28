import os
import random
os.mkdir('/Users/mac/Desktop/papka4')
i = 0
while i < 5:
	a = random.randint(1, 100000)
	os.mknod(f'/Users/mac/Desktop/papka4/t{a}.txt')
	i += 1