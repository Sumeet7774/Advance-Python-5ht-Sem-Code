# a=10
# b=0
# c=a/b

# print(c)

# try:
#     result=10/0
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")


# try:
#     numerator=10
#     denominator=0
    
#     result=numerator/denominator
    
#     print(result)
    
# except:
#     print("Error: Denominator cannot be 0.")



# try:
#     num = int(input("Enter a number: "))
# except TypeError:
#     print("Error: Invalid input. Please enter a integer")


# try:
#     with open("non_existent_file.txt", "r") as file:
#         content=file.read()
# except IOError:
#     print("Error: File not found")


# try:
#     my_list = [1,2,3]
#     print(my_list[5])
# except IndexError:
#     print("Error: Index out of bound")    


# try:
#     my_dict = {"name": "John", "age": 20}
#     print(my_dict["gender"])
# except:
#     print("Error: Key not found in the dictionary")


# try:
#     print(x)
# except NameError:
#     print("Error: Variable x is not defined")


# try:
#     result = 10 + "5"
# except TypeError:
#     print("Error: Cannot add integer and string")
    
    
# try:
#     result = "Hello"/2
# except TypeError:
#     print("Error: Cannot add integer and string")


# try:
#     num = int(123, base=10)
#     print(num)
# except TypeError:
#     print("Error: Cannot add integer and string")
    
   
# try:
#     num = int(input("Enter a number: "))
#     result = 10/num
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero")
# except ValueError:
#     print("Error: Value Error") 


# try:
#     #Code that may cause an error
#     file = open("example.txt", "r")
#     #Perform some file operations
# finally:
#     file.close()   #File will be closed regardless of exceptions
 
        
# try:
#     num = int(input("Enter a number: "))
#     result = 10/num
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero")
# except ValueError:
#     print("Error: Invalid input. Please enter a valid integer.")        
# else:
#     print("Division result: ", result)


