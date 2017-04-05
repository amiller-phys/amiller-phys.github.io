from random import random 

N = 5
R = .25
reps = 1000000
accum = 0
for rep in range(reps):
	Arrivals = []
	for i in range(N):
		Arrivals.append(random())
	fail = 0
	for i in range(N):
		for j in range(N):
			if abs(Arrivals[i]-Arrivals[j]) > R:
				fail = 1
	if fail == 0:
		accum += 1

print(accum/reps)
