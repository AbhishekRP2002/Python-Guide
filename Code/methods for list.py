# # Methods available on List
# 1. append(): Adds an element at the end of the list
# 2. count(): Returns the number of elements with the specified value
# 3. index(): Returns the index of the first element with the specified value
# 4. sort(): sorts the list
# 5. reverse(): reverse the list
# 6. pop(): removes item from the list
# 7. insert(): inserts item at the specified index
# 8. remove(): removes item from the list
# 9. clear(): removes all items from the list
# 10. copy(): returns a copy of the list
# 11. extend(): adds the elements of a list (or any iterable), to the end of the current list
# 12. len(): returns the length of the list
# 13. max(): returns the largest item in the list
# 14. min(): returns the smallest item in the list
# 15. sum(): returns the sum of all items in the list
# 16. any(): returns True if any item in the list is True
# 17. all(): returns True if all items in the list are True
# 18. enumerate(): returns an enumerate object. It contains the index and value of all the items as tuples in the list.
# 19. sorted(): returns a new sorted list from the items in the iterable
list=[1,2,3,4,5,6,7,8,9,10]
print(list)
print(sum(list))
list.append(4)
print(list)
cnt = list.count(4)
print(cnt)
ind = list.index(5)
print(ind)
list.reverse()
print(list)
listInsert = list.insert(2, 11)
print(list)
print(list.pop(2)) # removes item from the list and takes index as parameter
print(max(list))
maxVal = list[0]
for i in range(0, len(list)):
    if list[i] > maxVal:
        maxVal = list[i]
print(maxVal)

minVal = list[0]
for i in range(0, len(list)):
    if list[i]<minVal:
        minVal = list[i]
print(minVal)
    