


"""

The rmdir() Method
The rmdir() method deletes the directory, which is passed as an argument in the method.

Before removing a directory, all the contents in it should be removed.

Syntax
os.rmdir('dirname')
Example
Following is an example to remove the "/tmp/test" directory. It is required to give fully qualified name of the directory, otherwise it would search for that directory in the current directory.


"""

import os

# This would  remove "/tmp/test"  directory.
os.rmdir( "/tmp/test"  )



