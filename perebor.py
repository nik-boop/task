from itertools import permutations
towns = [
	[0, 6, 4, 8, 7,14],
	[6, 0, 7, 11, 7,10],
	[4, 7, 0, 4, 3,10],
	[8, 11, 4, 0, 5,11],
	[7, 7, 3, 5, 0,7],
	[14,10,10,11,7,0]
]
a = list(permutations(list(range(len(towns[0])))[1:]))
s = []
for i in a:
    s.append([0]+list(i)+[0])
print(s)

le =[]

summ = -1
path = []
for i in s:
	sm = 0
	for a in range(len(i)-1):
		print(towns[i[a]][i[a+1]])
		sm += towns[i[a]][i[a+1]]
	if sm < summ or summ == -1:
		path = i
		summ = sm
for i in range(len(path)):
	path[i]+=1
print(path,summ)
#1-2-6-5-4-3-1
#0-1-5-4-3-2-0
#36
