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
