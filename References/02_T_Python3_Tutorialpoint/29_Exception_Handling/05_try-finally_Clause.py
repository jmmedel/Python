


"""

The try-finally Clause
You can use a finally: block along with a try: block. The finally: block is a place to put any code that must execute, whether the try-block raised an exception or not. The syntax of the try-finally statement is this −

try:
   You do your operations here;
   ......................
   Due to any exception, this may be skipped.
finally:
   This would always be executed.
   ......................
Note − You can provide except clause(s), or a finally clause, but not both. You cannot use else clause as well along with a finally clause.


"""

try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
finally:
   print ("Error: can\'t find file or read data")
   fh.close()

"""
If you do not have permission to open the file in writing mode, then this will produce the following result −

Error: can't find file or read data


"""


