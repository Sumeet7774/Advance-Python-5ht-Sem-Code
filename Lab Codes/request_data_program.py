file = open("student_info.txt", "r")

rollno = input("Enter your rollno: ")
rollno+="\n"
lines = file.readlines()

for line in lines:
    if(line==rollno):
        print(lines)
        
        
        
    