# option 1
# Use reverse funtion
numbers = [5,7,8,1,2,3,6,9]

def reverse_list(numbers):
    numbers.reverse()

    return numbers
print(reverse_list(numbers))

# option 2
# Create a list of numbers
# return a list and start at -1 and step -1

def reverse_list(numbers):
    return numbers[-1::-1]

print(reverse_list(numbers))

