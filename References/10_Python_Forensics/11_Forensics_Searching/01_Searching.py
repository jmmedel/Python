


"""

Python Forensics - Searching

Searching is certainly one of the pillars of forensic investigation. Nowadays, search is only as good as the investigator who is running the evidence.

Searching a keyword from the message plays a vital role in forensics, when we search for an evidence with the help of a keyword. The knowledge of what is to be searched in a particular file along with the ones in deleted files requires both experience and knowledge.

Python has various built-in mechanisms with standard library modules to support search operation. Fundamentally, investigators use the search operation to find answers to questions such as "who", "what", "where", "when", etc.

Example
In the following example, we have declared two strings and then, we have used the find function to check whether the first string contains the second string or not.


"""


str1 = "This is a string example for Computational forensics of gathering evidence!";
str2 = "string";

print (str1.find(str2))
print (str1.find(str2, 10))
print (str1.find(str2, 40))



"""

“find” function in Python helps in searching a keyword in a message or a paragraph. This is critical in collecting appropriate evidence.


"""

