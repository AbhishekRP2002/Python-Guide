nums = [5,10,20,25]
print(nums[0])
print(nums[2])
print("Negative indexing starts from the end of the list:")
print("Index:-1", nums[-1]) # last element or first element from the end
print("Index:-3",nums[-3]) # third element from the end
# Negative index can be used to give elements from the end of the list

#slicing of lists
lst = [1,2,3,4,5,6,7,8,9,10]
sublst = lst[0:3]
print(sublst)
sublst2 = lst[3:len(lst)] # start index  = 4 and end index(exclusive)  = 10
print("Length of the list is: ", len(lst))
print(sublst2)


# We can use negative indexing in slicing as well
lst = [1,2,3,4,5,6,7,8,9,10]
temp = lst[-5:-1]
temp2 = lst[:-5]
temp3 = lst[-5:]
print(temp)
print(temp2)
print(temp3)

# Using step in slicing
lst = [1,2,3,4,5,6,7,8,9,10]
temp4 = lst[1:10:2]
print(temp4)

#Reverse  a list using slicing
nums = [1,2,3,4,5,6,7,8,9,10]
revNums = nums[::-2]
revNums2 = nums[::-1]
print(revNums)
print(revNums2)

#change multiple items in list to
nums = [1,2,3,4,5,6,7,8,9,10]
nums[:5] = [0,0,0,0,0]
print(nums)

#slicig also works with strings and tuples or any commplex data type whhich uses index for accessing elements