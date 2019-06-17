#reverse
n=int(input())
l=[int(i) for i in input().split()]
l=[bin(i)[2:] for i in  l]
l.sort(reverse=True)
m=[int(i,2) for i in l]
for i in m:
	print(i)
