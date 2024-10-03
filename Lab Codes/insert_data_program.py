while True:
    name=input("Enter name: ")
    roll_no=input("Enter roll number: ")
    division=input("Enter division: ")
    group=input("Enter group: ")

    with open("student_info.txt",'a') as file:
        file.write(name+"\n")
        file.write(roll_no+"\n")
        file.write(division+"\n")
        file.write(group+"\n")
        file.write("\n")

    ans=input("Enter Other Values! (y/n) ")
    
    if ans.lower()=="n":
        break