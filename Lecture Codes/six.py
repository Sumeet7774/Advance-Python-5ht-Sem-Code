fp = open("file.txt", "rb")
a = fp.read(fp.seek(-3,2))
print(a)