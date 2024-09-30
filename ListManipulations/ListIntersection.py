
list1 = [[2,3,4,2,5,6,3,7,7],[1,7,9,0,4,2,3,5]]

def list_intersection():
    newList = set().union(*list1)
    return newList

print(list_intersection())