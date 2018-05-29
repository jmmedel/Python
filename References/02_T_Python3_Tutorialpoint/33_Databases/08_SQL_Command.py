

"""


COMMIT Operation
Commit is an operation, which gives a green signal to the database to finalize the changes, and after this operation, no change can be reverted back.

Here is a simple example to call the commit method.

db.commit()
ROLLBACK Operation
If you are not satisfied with one or more of the changes and you want to revert back those changes completely, then use the rollback() method.

Here is a simple example to call the rollback() method.

db.rollback()
Disconnecting Database
To disconnect the Database connection, use the close() method.

db.close()
If the connection to a database is closed by the user with the close() method, any outstanding transactions are rolled back by the DB. However, instead of depending on any of the DB lower level implementation details, your application would be better off calling commit or rollback explicitly.

Handling Errors
There are many sources of errors. A few examples are a syntax error in an executed SQL statement, a connection failure, or calling the fetch method for an already canceled or finished statement handle.

The DB API defines a number of errors that must exist in each database module. The following table lists these exceptions.

S.No.	Exception & Description
1	
Warning

Used for non-fatal issues. Must subclass StandardError.

2	
Error

Base class for errors. Must subclass StandardError.

3	
InterfaceError

Used for errors in the database module, not the database itself. Must subclass Error.

4	
DatabaseError

Used for errors in the database. Must subclass Error.

5	
DataError

Subclass of DatabaseError that refers to errors in the data.

6	
OperationalError

Subclass of DatabaseError that refers to errors such as the loss of a connection to the database. These errors are generally outside of the control of the Python scripter.

7	
IntegrityError

Subclass of DatabaseError for situations that would damage the relational integrity, such as uniqueness constraints or foreign keys.

8	
InternalError

Subclass of DatabaseError that refers to errors internal to the database module, such as a cursor no longer being active.

9	
ProgrammingError

Subclass of DatabaseError that refers to errors such as a bad table name and other things that can safely be blamed on you.

10	
NotSupportedError

Subclass of DatabaseError that refers to trying to call unsupported functionality.

Your Python scripts should handle these errors, but before using any of the above exceptions, make sure your MySQLdb has support for that exception. You can get more information about them by reading the DB API 2.0 specification.

 Previous Page Next Page  




"""
