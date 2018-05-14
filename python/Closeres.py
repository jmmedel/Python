#closures
#So what are closures good for?

#Closures can avoid the use of global values and provides some form of data hiding.
# It can also provide an object oriented solution to the problem.
#When there are few methods (one method in most cases) to be implemented i
#a class, closures can provide an alternate and more elegant solutions. But when the number of attributes and methods get larger, better implement a class.

def get_func_mult_by_num(num):
   
    def multi_by(value):
        return num * value
        
    return multi_by

generated_func = get_func_mult_by_num(5)
print("5 * 10 = ", generated_func(10))

