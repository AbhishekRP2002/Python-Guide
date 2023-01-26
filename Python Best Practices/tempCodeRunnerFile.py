    
num = int(input("Enter the number:"))
i = 2
while i < num:
    if num%i==0:
        print("Number is not a prime number")
    i+=1
else:
    print("Number is a prime number")