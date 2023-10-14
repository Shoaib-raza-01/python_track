# if we dont know how many args will come we use variable length argument

# def sum(*b):
#     c = 0 
#     for i in b:
#         c += i
#     print(c)
# sum(1,2,3,4,5,6)



# =============================================================================



# secondly we can also pass agruments in a key value pairs called as keyword argument

# def details(**data):
#     for i,j in data.items():
#         print(i,j)

# details(name= "Shoaib", age= 21 , num = 7203658954, city = "Mumbai")



# ================================================================================



# using local and global variables in same function 
# we have a keyword  global and a function globals() to use in different cases

# a = 10
# b= 20
# print("before updation : ", a)

# def func():
#     # global a   # without global a will become local and local variables are give more preference 

#     a= 13
#     print("inside function : " , a)
#     print("printing global while having a local with same name : " , globals()['a'])

# func()
# print("outside function : " ,a)

# =================================================================================


# lmabda function | anonymous function

# f = lambda a,b : a + b
# result = f(23,34)
# print(result)