listNums = [1,2,3,4,5,6,7,8,9,10]
for i in listNums:
    if i%2 == 0:
        print(i)
    else:
        print("Odd number" , i)
        

languages = ['Python', 'Java', 'C++', 'C#', 'JavaScript']
#Case 1
for lang in languages:
    if lang == 'C++':
        print(lang, 'found')
        break
else:
    print("Unknown language")
    
#Case 2    
for lang in languages:
    if lang == 'Rust':
        print(lang, 'found')
        break
else:
    print("Unknown language")
    
#Case 3 using Flag
languages = ['Python', 'Java', 'C++', 'C#', 'JavaScript']
found = False
finalLang = ''
for lang in languages:
    if lang == 'Python':
        found = True
        finalLang = lang
        break
    
if found:
    print(finalLang , " Language Found")
else:
    print("Unknown language")
    
    
    
    
num = int(input("Enter the number:"))
i = 2
while i < num:
    if num%i==0:
        print("Number is not a prime number")
    i+=1
else:
    print("Number is a prime number")