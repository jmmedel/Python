

"""

There is one more example where argument is being passed by reference and the reference is being overwritten inside the called function.

"""


# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4] # This would assi new reference in mylist
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)


"""

The parameter mylist is local to the function changeme. Changing mylist within the function does not affect mylist. The function accomplishes nothing and finally this would produce the following result −

Values inside the function:  [1, 2, 3, 4]
Values outside the function:  [10, 20, 30]


"""

