


"""

Python 3 - MySQL Database Access

The Python standard for database interfaces is the Python DB-API. Most Python database interfaces adhere to this standard.

You can choose the right database for your application. Python Database API supports a wide range of database servers such as −

GadFly
mSQL
MySQL
PostgreSQL
Microsoft SQL Server 2000
Informix
Interbase
Oracle
Sybase
SQLite
Here is the list of available Python database interfaces − Python Database Interfaces and APIs. You must download a separate DB API module for each database you need to access. For example, if you need to access an Oracle database as well as a MySQL database, you must download both the Oracle and the MySQL database modules.

The DB API provides a minimal standard for working with databases using Python structures and syntax wherever possible. This API includes the following −

Importing the API module.
Acquiring a connection with the database.
Issuing SQL statements and stored procedures.
Closing the connection
Python has an in-built support for SQLite. In this section, we would learn all the concepts using MySQL. MySQLdb module, a popular interface with MySQL is not compatible with Python 3. Instead, we shall use PyMySQL module.

What is PyMySQL ?
PyMySQL is an interface for connecting to a MySQL database server from Python. It implements the Python Database API v2.0 and contains a pure-Python MySQL client library. The goal of PyMySQL is to be a drop-in replacement for MySQLdb.

How do I Install PyMySQL?
Before proceeding furthur, you make sure you have PyMySQL installed on your machine. Just type the following in your Python script and execute it −



"""

import PyMySQL


"""

Note − Make sure you have root privilege to install the above module.

Database Connection
Before connecting to a MySQL database, make sure of the following points −

You have created a database TESTDB.

You have created a table EMPLOYEE in TESTDB.

This table has fields FIRST_NAME, LAST_NAME, AGE, SEX and INCOME.

User ID "testuser" and password "test123" are set to access TESTDB.

Python module PyMySQL is installed properly on your machine.

You have gone through MySQL tutorial to understand MySQL Basics.

Example
Following is an example of connecting with MySQL database "TESTDB" −


"""


#!/usr/bin/python3

import PyMySQL

# Open database connection
db = PyMySQL.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()


"""

While running this script, it produces the following result.

Database version : 5.5.20-log
If a connection is established with the datasource, then a Connection Object is returned and saved into db for further use, otherwise db is set to None. Next, db object is used to create a cursor object, which in turn is used to execute SQL queries. Finally, before coming out, it ensures that the database connection is closed and resources are released.

"""

