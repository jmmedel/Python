


"""


Performing Transactions
Transactions are a mechanism that ensures data consistency. Transactions have the following four properties −

Atomicity − Either a transaction completes or nothing happens at all.

Consistency − A transaction must start in a consistent state and leave the system in a consistent state.

Isolation − Intermediate results of a transaction are not visible outside the current transaction.

Durability − Once a transaction was committed, the effects are persistent, even after a system failure.

The Python DB API 2.0 provides two methods to either commit or rollback a transaction.

Example
You already know how to implement transactions. Here is a similar example −


# Prepare SQL query to DELETE required records
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()
   


"""
