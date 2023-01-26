import math 



nums = []

for i in range(1,6):
    nums.append(2**i)
    
print(nums)

#List comprehension
nums2 = [2**i for i in range(1,6)]
print(nums2)

sqNums =  [4, 16 , 64 , 100 , 256]
new_list = [math.sqrt(n) for n in sqNums]
print(new_list)
new_list2 = [math.sqrt(n) for n in sqNums if n > 50]
new_list3 = [math.sqrt(n) for n in sqNums if n%2==0]
print(new_list2)
print(new_list3)


team1 = ["Virat", "Rohit", "Dhoni"]
team2 = ["Rahul", "Pant", "Shami"]
new_team =[(x,y) for x in team1 for y in team2]
print(new_team)

#Set comprehension
word = "programming"
alphabet = {x for x in word}
print(alphabet)
alphabet = {x for x in word if x > 'a'}
print(alphabet)

# Dictionary comprehension

nums = [1,2,3,4,5,6,7]

square = dict()

for i in nums:
    square[i] = i**2
print(square)

square_dict = {num:num**2 for num in nums}
print(square_dict)

