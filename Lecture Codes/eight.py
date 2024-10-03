#first method

# def square(x):
#     return x**2

# list = [2,4,5,7,9]
# z = []

# for y in list:
#     z.append(square(y))
# print(z)


#second method
# numbers = [2,4,5,7,9]

# def square(x):
#     return x**2

# sq_list = list(map(square,numbers))
# print(sq_list)

# -------------------------------------------------

# def cube(y):
#     return y*y*y

# g = lambda x: x*x*x 
# print(g(7))
# print(cube(5))


# def add(x,y):
#     return x+y

# print(lambda x,y: x+y)


# numbers = [1, 2, 3, 4, 5]

# sq_list = list(map(lambda x: x**2, numbers))
# print(sq_list)


# celcius = [39.2,45.5,67.9,38.3]
# farenheit = list(map(lambda x: ((9/5)*x)+32,celcius))
# print(farenheit)