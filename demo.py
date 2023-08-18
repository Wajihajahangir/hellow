l=[]
a=int(input('Enter no of items'))
for i in range(a):
 print('Enter item # ', i+1)    
 b=input()
 l.append(b)
 f=open("hellow.txt",mode="w")
print(l)
f.writelines(l)
f.close()