from random import random
max = 100000
total = 0
for n in range(max):
	total += abs(random()-random()) <= 0.1
ans = round(total/max, 2)
print(ans)	