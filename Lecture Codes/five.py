file = open("bennet.txt", "r")

for each in file:
    print (each)
    
print (file.read())
print (file.read(5))

file1 = open("bennett.txt", 'a')
file.write("This will add this line")
file.close()

#this will give error as there is no file as "bennett.txt"