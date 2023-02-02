# format(): format method formats the specifiedvalue(s) and insert them inside the string's placeholder.the placeholder is defined using curly brackets: {}.

# {} indicate karta hai ki run time pe value add hona wala hai inside the placeholder

line = "My name is {} and I am {} years old".format("Gaurav", 21)
print(line)

line = "My name is {0} and I am {1} years old".format("sachin", 21)
print(line)

line = "hey {1} {0}".format("Gaurav", "Kumar")
print(line)

line = "hey {a} cute lol {b}".format(a = "Gaurav", b = "Kumar")
print(line)