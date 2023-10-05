def multiply(num1, num2):
    result = 0
    for i in range(num2):
        result += num1
    return result


num1 = 2
num2 = 3
product = multiply(num1, num2)
print("Product:", product)