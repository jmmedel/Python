

"""
Python 3 - String encode() Method
Advertisements
 Previous Page Next Page  
Description
The encode() method returns an encoded version of the string. Default encoding is the current default string encoding. The errors may be given to set a different error handling scheme.

Syntax
Following is the syntax for encode() method −

str.encode(encoding = 'UTF-8',errors = 'strict')
Parameters
encoding − This is the encodings to be used. For a list of all encoding schemes please visit − Standard Encodings.

errors − This may be given to set a different error handling scheme. The default for errors is 'strict', meaning that encoding errors raise a UnicodeError. Other possible values are 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' and any other name registered via codecs.register_error().

Return Value
Decoded string.

Example"""

import base64

Str = "this is string example....wow!!!"
Str = base64.b64encode(Str.encode('utf-8',errors = 'strict'))

print ("Encoded String: " , Str)
print ("Decoded String: " + Str.decode('utf-8','strict'))

