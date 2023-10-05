def reverse(start, end):
    while start >= end:
        print(start)
        start -= 2

def ispalindrome(num):
    num = str(num)
    return num == num[::-1]

num = 101
print("is", num, "a palindrome", ispalindrome(num))
start = 10
end = 0
reverse(start, end)