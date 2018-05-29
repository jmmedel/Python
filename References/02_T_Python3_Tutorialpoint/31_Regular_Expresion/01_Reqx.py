


"""

Python 3 - Regular Expressions
Advertisements
 Previous Page Next Page  
A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern. Regular expressions are widely used in UNIX world.

The module re provides full support for Perl-like regular expressions in Python. The re module raises the exception re.error if an error occurs while compiling or using a regular expression.

We would cover two important functions, which would be used to handle regular expressions. Nevertheless, a small thing first: There are various characters, which would have special meaning when they are used in regular expression. To avoid any confusion while dealing with regular expressions, we would use Raw Strings as r'expression'.

Basic patterns that match single chars
S.No.	Expression & Matches
1	
a, X, 9, <

ordinary characters just match themselves exactly.

2	
. (a period)

matches any single character except newline '\n'

3	
\w

matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_].

4	
\W

matches any non-word character.

5	
\b

boundary between word and non-word

6	
\s

matches a single whitespace character -- space, newline, return, tab

7	
\S

matches any non-whitespace character.

8	
\t, \n, \r

tab, newline, return

9	
\d

decimal digit [0-9]

10	
^

matches start of the string

11	
$

match the end of the string

12	
\

inhibit the "specialness" of a character.

Compilation flags
Compilation flags let you modify some aspects of how regular expressions work. Flags are available in the re module under two names, a long name such as IGNORECASE and a short, one-letter form such as I.

S.No.	Flag & Meaning
1	
ASCII, A

Makes several escapes like \w, \b, \s and \d match only on ASCII characters with the respective property.

2	
DOTALL, S

Make, match any character, including newlines

3	
IGNORECASE, I

Do case-insensitive matches

4	
LOCALE, L

Do a locale-aware match

5	
MULTILINE, M

Multi-line matching, affecting ^ and $

6	
VERBOSE, X (for ‘extended’)

Enable verbose REs, which can be organized more cleanly and understandably

The match Function
This function attempts to match RE pattern to string with optional flags.

Here is the syntax for this function −

re.match(pattern, string, flags = 0)
Here is the description of the parameters −

S.No.	Parameter & Description
1	
pattern

This is the regular expression to be matched.

2	
string

This is the string, which would be searched to match the pattern at the beginning of string.

3	
flags

You can specify different flags using bitwise OR (|). These are modifiers, which are listed in the table below.

The re.match function returns a match object on success, None on failure. We usegroup(num) or groups() function of match object to get matched expression.


S.No.	Match Object Method & Description
1	
group(num = 0)

This method returns entire match (or specific subgroup num)

2	
groups()

This method returns all matching subgroups in a tuple (empty if there weren't any)

Example


"""


import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")

"""

When the above code is executed, it produces the following result −

matchObj.group() :  Cats are smarter than dogs
matchObj.group(1) :  Cats
matchObj.group(2) :  smarter

"""
