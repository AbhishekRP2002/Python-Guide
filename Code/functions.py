#Python is a multi paradigm language and it supports functional programming

def sum(arg1 , arg2):
    return (arg1 + arg2)

a = 10 
b = 12
var = sum(a , b)
print(var)

# default arguments *args and **kwargs in Python

def student(name = "Unknown Name" , arg1 = 0):
    print("Student Name is " , name)
    print("Arg1 is " , arg1)
    
student("Rahul" , 10)
student()

# Passing a list as an argument and key value pair as an argument

def info(name , age , *marks):
    print("Student Name is " , name)
    print("Age is " , age)
    print("Marks in  List form are " , marks)
    print("Marks are " ,*marks)
    for i in marks:
        print(i)
        
info("Rahul" , 20 , 10 , 20 , 30 , 40 , 50)

def student_info(name , age , **marks):
    print("Student Name is " , name)
    print("Age is " , age)
    print("Marks " , *marks)
    print("Marks " , marks)
    for i in marks:
        print(i)
    for key,value in marks.items():
        print(key,"-",value)
        
        
student_info("Rahul" , 20 , math = 10 , science = 20 , english = 30 , hindi = 40 , social = 50)

#lambda function in python

def double(x):
    return x*2
def add(x,y):
    return x+y
def product(x,y ,z):
    return x*y*z

double = lambda x : x*2
add = lambda x,y : x+y
product = lambda x, y, z : x*y*z

print(double(10))
print(product(10,20,30))

#Filter , map and reduce function in python

my_list = [1,2,3,4,5,6,7,8,9,10]
my_list2 = [1,2,3,4,5,6,7,8,9,10]
a = map(lambda x:x*5 , my_list)
print(list(a))
b = map(lambda x, y: x+y , my_list , my_list2)
print(list(b))

# Map function in python takes a function and a list as an argument and returns a list

c = filter(lambda x:x%2==0 , my_list)
print(list(c))

# reduce function in python takes a function and a list as an argument and returns a single value

# filter function in python takes a function and a list as an argument and returns a list.The function can be any function which returns a boolean value

from functools import reduce
my_list = [1,2,3,4,5,6,7,8,9,10]
e = reduce(lambda x,y:x+y , my_list)
print(e)
print(sum(my_list))