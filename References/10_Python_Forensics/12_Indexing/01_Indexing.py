


"""

Python Forensics - Indexing

Indexing actually provides the investigator have a complete look at a file and gather potential evidence from it. The evidence could be contained within a file, a disk image, a memory snapshot, or a network trace.

Indexing helps in reducing time for time-consuming tasks such as keyword searching. Forensic investigation also involves interactive searching phase, where the index is used to rapidly locate keywords.

Indexing also helps in listing the keywords in a sorted list.

Example
The following example shows how you can use indexing in Python.


"""


aList = [123, 'sample', 'zara', 'indexing'];

print ("Index for sample : ", aList.index('sample'))
print ("Index for indexing : ", aList.index('indexing'))

str1 = "This is sample message for forensic investigation indexing";
str2 = "sample";

print ("Index of the character keyword found is " )
print (str1.index(str2))
