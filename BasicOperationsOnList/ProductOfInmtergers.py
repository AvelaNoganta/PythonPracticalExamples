numbers = [3, 9, 7, 5, 8]


def product_list(numbers):

    product = 1
    for i in numbers:
        product *= i
    return product


print(product_list(numbers))