# Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
def main():
    num1 = 5
    num2 = 10
    product = num1 * num2
    if (product) <= 1000:
        return print(product)
    else:
        return print(num1 + num2)


main()
