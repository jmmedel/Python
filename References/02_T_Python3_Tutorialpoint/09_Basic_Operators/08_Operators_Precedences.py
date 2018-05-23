
"""
Python 3 - Operators Precedence Example
The following table lists all operators from highest precedence to the lowest.

S.No.	Operator & Description
1	
**

Exponentiation (raise to the power)

2	
~ + -

Ccomplement, unary plus and minus (method names for the last two are +@ and -@)
3	
* / % //

Multiply, divide, modulo and floor division

4	
+ -

Addition and subtraction

5	
>> <<

Right and left bitwise shift

6	
&

Bitwise 'AND'

7	
^ |

Bitwise exclusive `OR' and regular `OR'

8	
<= < > >=

Comparison operators

9	
<> == !=

Equality operators

10	
= %= /= //= -= += *= **=

Assignment operators

11	
is is not

Identity operators

12	
in not in

Membership operators

13	
not or and

Logical operators

Operator precedence affects the evaluation of an expression.

For example, x = 7 + 3 * 2; here, x is assigned 13, not 20 because the operator * has higher precedence than +, so it first multiplies 3*2 and then is added to 7.

Here, the operators with the highest precedence appear at the top of the table, those with the lowest appear at the bottom.

Example"""
a = 20
b = 10
c = 15
d = 5

print ("a:%d b:%d c:%d d:%d" % (a,b,c,d ))
e = (a + b) * c / d       #( 30 * 15 ) / 5
print ("Value of (a + b) * c / d is ",  e)

e = ((a + b) * c) / d     # (30 * 15 ) / 5
print ("Value of ((a + b) * c) / d is ",  e)

e = (a + b) * (c / d)    # (30) * (15/5)
print ("Value of (a + b) * (c / d) is ",  e)

e = a + (b * c) / d      #  20 + (150/5)
print ("Value of a + (b * c) / d is ",  e)
