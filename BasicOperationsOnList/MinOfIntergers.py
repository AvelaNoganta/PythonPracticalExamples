numbers = [6, 8, 0, 3, 8, 9, 12, 5]

def find_min(numbers):

    return min(numbers)


print(find_min(numbers))

#You can also use an if statement
def find_min(numbers):
    minValue = numbers[0]
    for m in numbers:
        if m < minValue:
            minValue = m

    return minValue
print(find_min(numbers))