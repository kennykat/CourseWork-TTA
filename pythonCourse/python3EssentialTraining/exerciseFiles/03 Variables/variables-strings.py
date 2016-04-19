#!/usr/local/bin/python3

#  strings are immutable objects
# \n - is an escape character // allows for a new line
# r - raw string // used in regular expressions // allows escape characters to be shown
def main():
    n = 42
    s = "This is a {} string!".format(n)
    # s = r"This is a\nstring"
    # s = "This is a\nstring"
    # s = "This is a string"
    print(s)

if __name__ == "__main__": main()
