

"""
Python's dictionaries are kind of hash-table type. They work like associative arrays or hashes found in Perl and consist of key-value pairs. A dictionary key can be almost any Python type, but are usually numbers or strings. Values, on the other hand, can be any arbitrary Python object.

Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([]). For example −"""

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values


"""
Dictionaries have no concept of order among the elements. It is incorrect to say that the elements are "out of order"; they are simply unordered.

Data Type Conversion
Sometimes, you may need to perform conversions between the built-in types. To convert between types, you simply use the type-names as a function.

There are several built-in functions to perform conversion from one data type to another. These functions return a new object representing the converted value.

S.No.	Function & Description
1	
int(x [,base])

Converts x to an integer. The base specifies the base if x is a string.

2	
float(x)

Converts x to a floating-point number.

3	
complex(real [,imag])

Creates a complex number.

4	
str(x)

Converts object x to a string representation.

5	
repr(x)

Converts object x to an expression string.

6	
eval(str)

Evaluates a string and returns an object.

7	
tuple(s)

Converts s to a tuple.

8	
list(s)

Converts s to a list.

9	
set(s)

Converts s to a set.

10	
dict(d)

Creates a dictionary. d must be a sequence of (key,value) tuples.

11	
frozenset(s)

Converts s to a frozen set.

12	
chr(x)

Converts an integer to a character.

13	
unichr(x)

Converts an integer to a Unicode character.

14	
ord(x)

Converts a single character to its integer value.

15	
hex(x)

Converts an integer to a hexadecimal string.

16	
oct(x)

Converts an integer to an octal string."""

