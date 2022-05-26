with open("a.txt",'r') as f:
    s=f.readlines()
    s1=0
    s2=0
    for i in range(1,len(s)):
        l=list(map(str,s[i].split()))
        s2+=float(l[2])
        s1+=float(l[1])
    print('average for USA=',s1/(len(s)-1))
    print('average for India=',s2/(len(s)-1))
