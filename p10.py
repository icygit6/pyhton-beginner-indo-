dic= {'nama':'Del','prodi':'ilmu komputer'}
print (dic['nama'])
for i in dic:
    print (dic[i])
for i,j in dic.items():
    print(i,j)

c= {1:10,2:20}
d= {3:30,4:40}
e={}
for i in (c,d):
   e.update(i)
   print(e)
kv= {'wili':'Dog','ku':'cat','mo':'monkey','ik':'fish','ko':'frog'}
for i,j in kv.items():
    print(i,'is a',j)
