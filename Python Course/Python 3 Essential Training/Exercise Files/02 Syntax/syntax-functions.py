#!/usr/local/bin/python3

def main():
    func(1)
    func()
    func(5)

def func(a=7):
    for i in range(a, 10):
        print(i, end=' ')
    print()
if __name__ == "__main__":main()
