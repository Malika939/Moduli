import random
names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
names2 = []
i=0
while i < 4:
	c = random.choice(names)
	print(c)
	i+=1
	names2.append(c)
	print(names2)