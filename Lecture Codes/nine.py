# numbers = [1,2,3,4,5,6,7,8]

# oddList = []
# evenList = []

# for i in numbers:
#     if i % 2 == 0:
#         evenList.append(i)
#     else:
#         oddList.append(i)

# print(oddList)
# print(evenList)

# ---------------------------------------------------------

# numbers = [1,2,3,4,5,6,7,8]

# result1 = list(filter(lambda x: x%2!=0, numbers))
# print(result1)

# result2 = list(filter(lambda x: x%2==0, numbers))
# print(result2)


# from functools import reduce
# numbers = [2,3,4,5]
# sum = reduce((lambda x,y: x+y), numbers, 4)
# print(sum)


# from functools import reduce
# f = lambda a,b: a if(a>b) else b
# r = reduce(f, [47,111,42,182,13])
# print(r)