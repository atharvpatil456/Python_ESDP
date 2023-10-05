class CharacterRemover:
    def __init__(self, inpstr, remove):
        self.inpstr = inpstr
        self.remove = remove

    def removeO(self):
        return self.inpstr.replace(self.remove, '')

inpstr = "welcome to metti"
remove = "i"

rem = CharacterRemover(inpstr, remove)

output = rem.removeO()
print("Output is:", output)



