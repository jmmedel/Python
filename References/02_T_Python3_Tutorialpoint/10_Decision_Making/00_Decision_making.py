"""
Python 3 - Decision Making
Decision-making is the anticipation of conditions occurring during the execution of a program and specified actions taken according to the conditions.

Decision structures evaluate multiple expressions, which produce TRUE or FALSE as the outcome. You need to determine which action to take and which statements to execute if the outcome is TRUE or FALSE otherwise.

Following is the general form of a typical decision making structure found in most of the programming languages −
Python programming language assumes any non-zero and non-null values as TRUE, and any zero or null values as FALSE value.

Python programming language provides the following types of decision-making statements.

S.No.	Statement & Description
1	if statements
An if statement consists of a boolean expression followed by one or more statements.

2	if...else statements
An if statement can be followed by an optional else statement, which executes when the boolean expression is FALSE.

3	nested if statements
You can use one if or else if statement inside another if or else if statement(s).

Let us go through each decision-making statement quickly.

Single Statement Suites
If the suite of an if clause consists only of a single line, it may go on the same line as the header statement.

Example
Here is an example of a one-line if clause −
var = 100
if ( var  == 100 ) : print ("Value of expression is 100")
print ("Good bye!")
Output
When the above code is executed, it produces the following result −

Value of expression is 100
Good bye!"""

var = 100
if ( var  == 100 ) : print ("Value of expression is 100")
print ("Good bye!")
