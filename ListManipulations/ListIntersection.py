
list1 = [2,3,4,2,5,6,3,7,7]
list2 = [1,7,9,0,4,2,3,5]
newList = []

# Loop through list 1
# loop through list 2
# if number in list1 is equal to number in list 2 add it to the new list
# if number already exists in the new list ignore it
# Return new list

def list_intersection(lst1, lst2):
    for i in list1:
        for s in list2:
         if i == s and i not in newList:
          newList.append(i)
    return newList

print(list_intersection(list1,list2))