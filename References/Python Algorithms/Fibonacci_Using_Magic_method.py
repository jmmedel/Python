# ---------- PROBLEM ----------
# Create a class that returns values from the Fibonacci
# sequence each time next is called
# Sample Output
# Fib : 1
# Fib : 2
# Fib : 3
# Fib : 5
# this time using __iter__ __next __ 

class Fibgenerator:
    
    def __init__(self):
        self.first = 0
        self.second = 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        fibnum = self.first + self.second
        self.first = self.second
        self.second = fibnum
        return fibnum
fibseq = Fibgenerator()

for i in range(10):
    print("Fib", next(fibseq))