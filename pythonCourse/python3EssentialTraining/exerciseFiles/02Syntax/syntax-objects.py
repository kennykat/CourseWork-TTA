#!/usr/local/bin/python3

## __init__ is a constructor(a method or a function inside a class)
class Egg:
    ## all methods in classes have (self) as the first argument
    def __init__(self, kind = "fried"):
        ## object variables reference to the object themselves
        self.kind = kind

    def whatKind(self):
        return self.kind

def main():
    fried = Egg()
    scrambled = Egg('scrambled')
    print(scrambled.whatKind())
    # print(fried.whatKind())

if __name__ == "__main__": main()
