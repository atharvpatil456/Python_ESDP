class Palindrome:
    def __init__(self, inpstr):
        self.inpstr = inpstr.lower()

    def ispalin(self):
        reversed_str = self.inpstr[::-1]
        return 1 if self.inpstr == reversed_str else 0

    def __del__(self):
        print("Palindrome instance deleted.")

inpstr = "abba"
checker = Palindrome(inpstr)
result = checker.ispalin()
print("Output:", result)

