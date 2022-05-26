4. WAP to write the numbers from 50 to 500 to the file d.txt.
All the numbers should be written in different lines
'''
with open("d.txt",'w') as f:
    for i in range(50,501):
        if i==500:
            f.write(str(i))
        else: f.write(str(i)+"\n")
