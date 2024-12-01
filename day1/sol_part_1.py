with open('req.txt','r') as f:
	a=f.readlines()
	c=len(a)
l1=[int(i.split()[0]) for i in a]
l2=[int(i.split()[1]) for i in a]
l1.sort()
l2.sort()
l3=[]
for i in range(c):
	print(l1[i],l2[i])
	l3.append(abs(l1[i]-l2[i]))
print(sum(l3))
