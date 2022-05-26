a=input("Enter a string: ")
myTitle(a)


def myCapitialize(s):
    a=list(s)
    x=ord(a[0])
    if x>=97 and x<=122:
        x=x-32
        a[0]=chr(x)
    a="".join(a)
    print(a)
