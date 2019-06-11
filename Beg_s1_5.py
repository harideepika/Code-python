#largest of 3 nos py
import sys
a,b,c = map(int,(input().split()))
#print(a,b,c)
if a>b and a>c : print(a)
elif b>c : print(b)
else : print(c)
