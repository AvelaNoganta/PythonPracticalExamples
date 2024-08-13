numbers = [4,6,7,3,5]

def sum_list(numbers):
    myTotal = 0
    for x in numbers:
        myTotal += x
    return myTotal
print(sum_list(numbers))

#Or I can use a sum() function
def sum_list(numbers):
    return sum(numbers)
print(sum_list(numbers))





