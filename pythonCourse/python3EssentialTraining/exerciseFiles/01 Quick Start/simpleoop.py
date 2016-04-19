#!/usr/local/bin/python3

# simple fibonacci series
# the sum of 2 elements defines the next set

# __init__ is a method/function constructor, it's called when f gets assigned
class Fibonacci():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def series(self):
        while(True):
            yield(self.b)
            self.a, self.b = self.b, self.a + self.b

# instantiating v v v
f = Fibonacci(0, 1)
for r in f.series():
    if r > 100: break
    print(r, end=' ')
