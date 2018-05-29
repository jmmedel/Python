


"""

Search and Replace
One of the most important re methods that use regular expressions is sub.

Syntax
re.sub(pattern, repl, string, max=0)
This method replaces all occurrences of the RE pattern in string with repl, substituting all occurrences unless max is provided. This method returns modified string.

Example



"""

import re

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print ("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print ("Phone Num : ", num)


"""

When the above code is executed, it produces the following result −

Phone Num :  2004-959-559
Phone Num :  2004959559


"""


"""

Regular Expression Modifiers: Option Flags
Regular expression literals may include an optional modifier to control various aspects of matching. The modifiers are specified as an optional flag. You can provide multiple modifiers using exclusive OR (|), as shown previously and may be represented by one of these −

S.No.	Modifier & Description
1	
re.I

Performs case-insensitive matching.

2	
re.L

Interprets words according to the current locale. This interpretation affects the alphabetic group (\w and \W), as well as word boundary behavior (\b and \B).

3	
re.M

Makes $ match the end of a line (not just the end of the string) and makes ^ match the start of any line (not just the start of the string).

4	
re.S

Makes a period (dot) match any character, including a newline.

5	
re.U

Interprets letters according to the Unicode character set. This flag affects the behavior of \w, \W, \b, \B.

6	
re.X

Permits "cuter" regular expression syntax. It ignores whitespace (except inside a set [] or when escaped by a backslash) and treats unescaped # as a comment marker.

Regular Expression Patterns
Except for the control characters, (+ ? . * ^ $ ( ) [ ] { } | \), all characters match themselves. You can escape a control character by preceding it with a backslash.

The following table lists the regular expression syntax that is available in Python −

Here is the list of regular expression syntax in Python.
Regular Expression Examples
Literal characters
S.No.	Example & Description
1	
python

Match "python".

Character classes
S.No.	Example & Description
1	
[Pp]ython

Match "Python" or "python"

2	
rub[ye]

Match "ruby" or "rube"

3	
[aeiou]

Match any one lowercase vowel

4	
[0-9]

Match any digit; same as [0123456789]

5	
[a-z]

Match any lowercase ASCII letter

6	
[A-Z]

Match any uppercase ASCII letter

7	
[a-zA-Z0-9]

Match any of the above

8	
[^aeiou]

Match anything other than a lowercase vowel

9	
[^0-9]

Match anything other than a digit

Special Character Classes
S.No.	Example & Description
1	
.

Match any character except newline

2	
\d

Match a digit: [0-9]

3	
\D

Match a nondigit: [^0-9]

4	
\s

Match a whitespace character: [ \t\r\n\f]

5	
\S

Match nonwhitespace: [^ \t\r\n\f]

6	
\w

Match a single word character: [A-Za-z0-9_]

7	
\W

Match a nonword character: [^A-Za-z0-9_]

Repetition Cases
S.No.	Example & Description
1	
ruby?

Match "rub" or "ruby": the y is optional

2	
ruby*

Match "rub" plus 0 or more ys

3	
ruby+

Match "rub" plus 1 or more ys

4	
\d{3}

Match exactly 3 digits

5	
\d{3,}

Match 3 or more digits

6	
\d{3,5}

Match 3, 4, or 5 digits

Nongreedy repetition
This matches the smallest number of repetitions −

S.No.	Example & Description
1	
<.*>

Greedy repetition: matches "<python>perl>"

2	
<.*?>

Nongreedy: matches "<python>" in "<python>perl>"

Grouping with Parentheses
S.No.	Example & Description
1	
\D\d+

No group: + repeats \d

2	
(\D\d)+

Grouped: + repeats \D\d pair

3	
([Pp]ython(,)?)+

Match "Python", "Python, python, python", etc.

Backreferences
This matches a previously matched group again −

S.No.	Example & Description
1	
([Pp])ython&\1ails

Match python&pails or Python&Pails

2	
(['"])[^\1]*\1

Single or double-quoted string. \1 matches whatever the 1st group matched. \2 matches whatever the 2nd group matched, etc.

Alternatives
S.No.	Example & Description
1	
python|perl

Match "python" or "perl"

2	
rub(y|le)

Match "ruby" or "ruble"

3	
Python(!+|\?)

"Python" followed by one or more ! or one ?

Anchors
This needs to specify match position.

S.No.	Example & Description
1	
^Python

Match "Python" at the start of a string or internal line

2	
Python$

Match "Python" at the end of a string or line

3	
\APython

Match "Python" at the start of a string

4	
Python\Z

Match "Python" at the end of a string

5	
\bPython\b

Match "Python" at a word boundary

6	
\brub\B

\B is nonword boundary: match "rub" in "rube" and "ruby" but not alone

7	
Python(?=!)

Match "Python", if followed by an exclamation point.

8	
Python(?!!)

Match "Python", if not followed by an exclamation point.

Special Syntax with Parentheses
S.No.	Example & Description
1	
R(?#comment)

Matches "R". All the rest is a comment

2	
R(?i)uby

Case-insensitive while matching "uby"

3	
R(?i:uby)

Same as above

4	
rub(?:y|le))

Group only without creating \1 backreference


"""


