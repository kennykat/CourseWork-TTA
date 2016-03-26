#!/usr/local/bin/python3

def main():
    print("This is the syntax.py file.")
    egg()

def egg():
    print("egg")

# this allows the script to run w/ the functions in any order you want
if __name__ == "__main__": main()


'''
# this won't run because when you call egg(),
# it has not been defined at the point where you call it

print("This is the syntax.py file.")
egg()

def egg():
    print("egg")
'''
