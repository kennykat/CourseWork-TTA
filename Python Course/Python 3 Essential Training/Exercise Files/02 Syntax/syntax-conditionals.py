#!/usr/local/bin/python3

## conditional execution
# def main():
#     a, b = 2, 1
#     # a, b = 1, 1
#     # a, b = 0, 1
#     if a < b:
#         print("a is less than b")
#     elif a > b:
#         print("a is greater than b")
#     else:
#         print("a is equal to b")
#
# if __name__ == "__main__": main()

## conditional expression
def main():
    a, b = 1, 1
    # a, b = 0, 1
    s = "less than" if a <b else "not less than"
    print(s)

if __name__ == "__main__": main()
