#Fibonacci_pythonic
a,b = 0, 1
for i in range(1,10):
    print(a)
    a, b = b, a+b
    
print("-"*10)
#  In an assignment statement, the right-hand side is
# always evaluated fully before doing the actual setting of variables. So,  
x = 1
y = 2
x,y = y,x+y # x,y = (2, 1 +2)
print(x)
print(y)
# this is how compiler work if you set a new variable its remember it 
print("-"*10)
x = 1
y = 2
x = y # x = 2 meaning you set a new variable to a new value
y = x+y # y = 2 + 2
print(x)
print(y)
