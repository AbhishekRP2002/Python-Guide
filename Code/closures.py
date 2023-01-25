# In python we can enclose one function inside another function
def outerFunction(text):
    print("Flow understand")
    def innerFunction():
        print("Inner function call" ,text)
    innerFunction()
    print("Outer function call" ,text)
    
outerFunction("Hello")


def pop(list):
    def last_element(list):
        return list[len(list)-1]
    list.remove(last_element(list))
    return list

a=[1,2,3,4,5,6,7,8]
b = pop(a)
print(b)
print(pop(a))
print(pop(a))

# Python closures
def nth_power(exponent):
    def pow_of(base):
        return pow(base, exponent)
    return pow_of

square = nth_power(2)
print(square(2))
print(square(3))