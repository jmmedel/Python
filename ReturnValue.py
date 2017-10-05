#return 2 or more value of return statement
def multi_div(x,y):
    # the first 1 is add ,second is minus milti and divide 
    return (x + y) ,(x - y),(x * y),(x / y)
add,minus,multi,divide = multi_div(5, 4)

print(add)
print(minus)
print(multi)
print(divide)