def double(x):
    return x*2
print(double(2))

double = lambda x: x*2
print(double(4))
# lambda functions are anonymous functions as they dont have a name
larger = lambda x, y : x if x > y else y
print(larger(10 ,15))


names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary' , 'Kunal' , 'Sachin' , 'Maddie']
names.sort()
print(names)
names.sort(key=lambda x: len(x))
print(names)

