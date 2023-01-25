# while loop example
i = 0
while i<5:
    print(i)
    i+=1
print("Done with loop")

# second example
num = 1
sum =0
print("Enter a number and press 0 to exit")
while num!=0:
    num = int(input("Enter a number: "))
    sum+=num
print("Sum of numbers is: ",sum)


# Python supports else statement with loop statements , once while loop is finished else statement is executed

i = 0
while i<=5:
    print("The value of i is: ",i)
    i+=1
else:
    print("i exceeded 5" , i)
    
# for loop example

A = [1,2,3,4,5,6,7,8,9,10] # list
B =(1,2,3,4,5,6,7,8,9,10) # tuple
C = {1,2,3,4,5,6,7,8,9,10} # set
D = "Hello World" # string
E = {
    "name":"John",
    "age":30,
    "roll":101
    } # dictionary


print(1 in A) # retruns true if 1 is present in list A
print(2 in B) # retruns true if 2 is present in tuple B and so on

for x in A:
    print(x)
else:
    print("Done with for loop")


for i in range(5):
    print(i)
    
for i in range(len(A)):
    print(i)
    
for i in range(2,10,2): # 2(inclusive) is starting , 10(exclusive) is ending and step is 2
    print(i)
