

"""

Python Forensics - Overview of Python
The codes written in Python look quite similar to the codes written in other conventional programming languages such as C or Pascal. It is also said that the syntax of Python is heavily borrowed from C. This includes many of the Python keywords which are similar to C language.

Python includes conditional and looping statements, which can be used to extract the data accurately for forensics. For flow control, it provides if/else, while, and a high-level for statement that loops over any "iterable" object.

if a < b: 
   max = b 
else: 
   max = a
The major area where Python differs from other programming languages is in its use of dynamic typing. It uses variable names that refer to objects. These variables need not be declared.

Data Types
Python includes a set of built-in data types such as strings, Boolean, numbers, etc. There are also immutable types, which means the values which cannot be changed during the execution.

Python also has compound built-in data types that includes tuples which are immutable arrays, lists, and dictionaries which are hash tables. All of them are used in digital forensics to store values while gathering evidence.

Third-party Modules and Packages
Python supports groups of modules and/or packages which are also called third-party modules (related code grouped together in a single source file) used for organizing programs.

Python includes an extensive standard library, which is one of the main reasons for its popularity in computational forensics.

Life Cycle of Python Code
At first, when you execute a Python code, the interpreter checks the code for syntax errors. If the interpreter discovers any syntax errors, then they are displayed immediately as error messages.

If there are no syntax errors, then the code is compiled to produce a bytecode and sent to PVM (Python Virtual Machine).

The PVM checks the bytecode for any runtime or logical errors. In case the PVM finds any runtime errors, then they are reported immediately as error messages.

If the bytecode is error-free, then the code gets processed and you get its output.

The following illustration shows in a graphical manner how the Python code is first interpreted to produce a bytecode and how the bytecode gets processed by the PVM to produce the output.


"""
