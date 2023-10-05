
def countdigits(num):
    return len(str(num))


num = int(input("Enter a number : "))
digits = countdigits(num)
if digits >= 5:
    print("Enter up to a 5 digit number.")
else:
    print("Number of digits entered :", digits)