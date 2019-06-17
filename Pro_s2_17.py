#include 
n,k=map(int,input().split())
l=[int(i) for i in input().split()]
l=[1 for i in range(n) for j in range(i+1,n) if l[i]+l[j]==k]
print("yes" if l else "no")
