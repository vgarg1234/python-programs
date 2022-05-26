
'''
3. WAP to copy the contents of file a.txt into c.txt
'''
f=open('a.txt','r')
g=open('c.txt','w')
st=f.read()
g.write(st)
f.close()
g.close()
