n=int(input())
s=input()
c=0
if s.count('I')==0:
    print(s.count('A'))
elif s.count('I')==1:
    print(1)
else:
    print(0)