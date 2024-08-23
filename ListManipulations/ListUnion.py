list1 = [2,3,4,2,5,6,3,7,7]
list2 = [1,7,9,0,4,2,3,5]

# Option 1
# Create a new list and return a set of each list to avoid duplicates

def list_union(lst1, lst2):
    newList = list(set(lst1) | set(lst2))
    return newList

print(list_union(list1,list2))

# Option 2
# Extend list1 with list2 then remove repeatition
def list_union(list1, list2): 
   list1.extend(list2)
   x = list(set(list1))
   return x
print(list_union(list1,list2))

# Option 3 
# Union list1 with list2 then remove repeatition
def list_union(list1, list2):
    newList = list(set().union(list1, list2))
    return newList
 
print(list_union(list1, list2))
