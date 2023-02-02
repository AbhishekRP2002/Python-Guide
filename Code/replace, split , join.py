# replace() - this method is used to replace a sub string with another sub string 
# syntax: string.replace(old, new, count)
# split() - this method is used to split a string into a list of substrings.
# These substrings will be returned as a list
# syntax: string.split('separator')
# join() - this method is used to join strings into one string
# syntax: "separator".join(list)

name = "Gaurav Kumar"
print(name)
new = "Nishant"
old = "Gaurav"
print(name.replace(old , new))
print(name.replace("Kumar" , new))


str = "how are you doing"
str1 = str.split(" ")
print(str1)
str2 = "how-are-you-doing"
print(str2.split("-"))


line1 = " ".join(str1)
line2 = "-".join(str1)
print(line1)
print(line2)