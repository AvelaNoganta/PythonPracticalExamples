numbers = [6, 8, 0, 3, 8, 9, 12, 8]

def find_max(numbers):

    return max(numbers)


print(find_max(numbers))

#You can also use an if statement
def find_max(numbers):
    maxValue = numbers[0]
    for m in numbers:
        if m > maxValue:
            maxValue = m

    return maxValue
print(find_max(numbers))

