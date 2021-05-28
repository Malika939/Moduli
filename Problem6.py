import random
names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# komanda = 3
# k1 = []
# k2 = []
# k3 = []
# k4 = []
# j = 1
# while j <= komanda:
# 	h = random.choice(names)
# 	k1.appened(h)
# 	for i in range(int(len(names))):
# 		if names[i] == h:
# 			del names[i]
# 			break
# 	j += 1
# print(k1)
n = int(len(names)/4)
random.shuffle(names)
print(names)
team1 = names[0:n]
team2 = names[n:n*2]
team3 = names[n*2:n*3]
team4 = names[n*3:]
print(team1)
print(team2)
print(team3)
print(team4)