

"""
Python 3 - String maketrans() Method
Description
The maketrans() method returns a translation table that maps each character in the intabstring into the character at the same position in the outtab string. Then this table is passed to the translate() function.

Note − Both intab and outtab must have the same length.

Syntax
Following is the syntax for maketrans() method −

str.maketrans(intab, outtab]);
Parameters
intab − This is the string having actual characters.

outtab − This is the string having corresponding mapping character.

Return Value
This method returns a translate table to be used translate() function.

Example
The following example shows the usage of maketrans() method. Under this, every vowel in a string is replaced by its vowel position −"""


intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "this is string example....wow!!!"
print (str.translate(trantab))
