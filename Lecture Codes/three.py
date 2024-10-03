fpx = open("hello.txt", "r")
fpy = open("new.txt", "w+")

for line in fpx:
    fpy.write(line)
    
fpy.seek(0)
print(fpy.read())
fpx.close()
fpy.close()