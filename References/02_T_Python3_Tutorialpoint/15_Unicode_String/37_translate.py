


"""
Python 3 String translate() Method
Description
The translate() method returns a copy of the string in which all characters have been translated using table (constructed with the maketrans() function in the string module), optionally deleting all characters found in the string deletechars.

Syntax
Following is the syntax for translate() method −

str.translate(table[, deletechars]);
Parameters
table − You can use the maketrans() helper function in the string module to create a translation table.

Return Value
This method returns a translated copy of the string.

Example
The following example shows the usage of translate() method. Under this, every vowel in a string is replaced by its vowel position."""

#from string import maketrans # Required to call maketrans function.

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!";
print (str.translate(trantab))


intab = "aeiou"
outtab = "12345"
deltab = "xm" #added line
trantab = str.maketrans(intab, outtab, deltab)

str = "this is string example....wow!!!"
print (str.translate(trantab))
