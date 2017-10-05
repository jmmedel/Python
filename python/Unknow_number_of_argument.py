# ---------- UNKNOWN NUMBER OF ARGUMENTS ----------
# We can receive an unknown number of arguments using
# the splat (*) operator
 
def sumAll(*args):
 
    total = 0
 
    for i in args:
        total += i
 
    return total
 
print("Sum :", sumAll(1,2,3,4))