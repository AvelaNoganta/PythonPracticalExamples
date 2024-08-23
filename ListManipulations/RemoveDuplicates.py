# Option 1
# Set: A collection of distinct (unique) well defined objects

numbers = [3,7,9,3,8,5,9,4,0,1,9]
set(numbers)

# Option 2
# I want to use a logic first to remove the duplicates
# Create a second list, and store the numbers we visit in it
# While visiting any number, check if it is already present in the second list
# If it is not present, so we add it to second list, 
# other wise we just ignore
# 

numbers = [3,7,9,3,8,5,9,4,0,1,9]

def remove_duplicates(numbers):
    visitedList = []
    for i in numbers:
        if i not in visitedList:
          # add it to visited list, and continue
          visitedList.append(i)
    return visitedList
      
print(remove_duplicates(numbers))
