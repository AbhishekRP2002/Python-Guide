'''
Multi-line docstrings are surrounded by triple quotes.
Docstrings are written just after the class or function definition.
Can be used for module documentation or while working in team

'''


def add(a, b):
    '''This function adds two numbers and returns the result'''
    return a + b

print(add(2,3))
print(add.__doc__)