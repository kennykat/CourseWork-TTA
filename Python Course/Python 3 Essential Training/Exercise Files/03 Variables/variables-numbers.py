#!/usr/local/bin/python3

# float and int are object constructors

def main():
    num = float(42) # creates the int into a float >> 42.0
    # num = int(42.9) # int creates the float as an int and loses the .9
    # num = 42 % 9 # modulo is the remainder, so 42/9 is 4 w/ remainder of 6
    # num = round(42 / 9, 2) # the 2 represents the digits you want to round up to
    # num = round(42 / 9) # rounds up
    # num = 42 // 9 # throws out integer
    # num = 42 / 9 # is a float
    # num = 42
    print(type(num), num)

if __name__ == "__main__": main()
