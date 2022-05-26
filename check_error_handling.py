try:
      a=int(input("enter any number"))
      b=int(input("enter any number"))
      print(a/b)
except nameError:
        print("YOU HAVE NOT DEFINED THE VALUE")
except zeroError:
        print("Division by zero is not possible")
else: 
        print("No error")
