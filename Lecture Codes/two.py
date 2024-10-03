fpx = open("x.txt","r")
fpy = open("y.txt", "w+")

for line in fpx:
    fpy.write(line)
    
fpy.seek(0)
print(fpy.read())