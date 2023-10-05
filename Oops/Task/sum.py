def sumdig(num):
    totalsum = 0
    while num > 0:
        totalsum += num % 10
        num //= 10
    return totalsum

num = int(input("Enter a number: "))
digits = sumdig(num)

if 20 <= digits <= 30:
    diff = abs(digits - 5)
    print("Sum of digits:", digits)
    print("Diff with 5 :", diff)
else:
    print("Sum of digits:", digits)
