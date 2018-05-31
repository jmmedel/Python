


"""

Python - Data Structure Tutorial

Computers store and process data with an extra ordinary speed and accuracy. So it is highly essential that the data is stored efficiently and can be accessed fast. Also the processing of data should happen in the smallest possible time but without losing the accuracy.

Data structures deal with how the data is organized and held in the memory when a program processes it. It is important to note that the data that is stored in the disk as part of persistent storages (like relational tables) are not referred as data structure here.

An Algorithm is step by step set of instruction to process the data for a specific purpose. So an algorithm utilizes various data structures in a logical way to solve a specific computing problem.

In this tutorial we will cover these two fundamental concepts of computer science using the Python programming language.

Audience
This tutorial is designed for Computer Science graduates as well as Software Professionals who are willing to learn data structures and algorithm programming in simple and easy steps using Python as a programming language.

Prerequisites
Before proceeding with this tutorial, you should have a basic knowledge of writing code in Python programming language, using any python IDE and execution of Python programs. If you are completely new to python then please refer our Python tutorial to get a sound understanding of the language.

Execute Python Programs
For most of the examples given in this tutorial you will find Try it option, so just make use of it and enjoy your learning.

Try following example using Try it option available at the top right corner of the below sample code box

Python - DS Introduction
Advertisements
 Previous Page Next Page  
Data Structure Overview
Data structures are fundamental concepts of computer science which helps is writing efficient programs in any language. Python is a high-level, interpreted, interactive and object-oriented scripting language using which we can study the fundamentals of data structure in a simpler way as compared to other programming languages.

In this chapter we are going to study a short overview of some frequently used data structures in general and how they are related to some specific python data types. There are also some data structures specific to python which is listed as another category.

General Data Structures
The various data structures in computer science are divided broadly into two categories shown below. We will discuss about each of the below data structures in detail in subsequent chapters.

LINER DATA STRUCTURES
These are the data structures which store the data elements in a sequential manner.

Array: It is a sequential arrangement of data elements paired with the index of the data element.
Linked List: Each data element contains a link to another element along with the data present in it.
Stack: It is a data structure which follows only to specific order of operation. LIFO(last in First Out) or FILO(First in Last Out).
Queue: It is similar to Stack but the order of operation is only FIFO(First In First Out).
Matrix: It is two dimensional data structure in which the data element is referred by a pair of indices.
NON-LINER DATA STRUCTURES
These are the data structures in which there is no sequential linking of data elements. Any pair or group of data elements can be linked to each other and can be accessed without a strict sequence.

Binary Tree: It is a data structure where each data element can be connected to maximum two other data elements and it starts with a root node.
Heap: It is a special case of Tree data structure where the data in the parent node is either strictly greater than/ equal to the child nodes or strictly less than it’s child nodes.
Hash Table: It is a data structure which is made of arrays associated with each other using a hash function. It retrieves values using keys rather than index from a data element.
Graph: .It is an arrangement of vertices and nodes where some of the nodes are connected to each other through links.
PYTHON SPECIFIC DATA STRUCTURES
These data structures are specific to python language and they give greater flexibility in storing different types of data and faster processing in python environment.

List: It is similar to array with the exception that the data elements can be of different data types. You can have both numeric and string data in a python list.
Tuple: Tuples are similar to lists but they are immutable which means the values in a tuple cannot be modified they can only be read.
Dictionary: The dictionary contains Key-value pairs as its data elements.
In the next chapters we are going to learn the details of how each of these data structures can be implemented using Python.

Python - DS Environment
Advertisements
 Previous Page Next Page  
Python is available on a wide variety of platforms including Linux and Mac OS X. Let's understand how to set up our Python environment.

Local Environment Setup
Open a terminal window and type "python" to find out if it is already installed and which version is installed.

Unix (Solaris, Linux, FreeBSD, AIX, HP/UX, SunOS, IRIX, etc.)
Win 9x/NT/2000
Macintosh (Intel, PPC, 68K)
OS/2
DOS (multiple versions)
PalmOS
Nokia mobile phones
Windows CE
Acorn/RISC OS
BeOS
Amiga
VMS/OpenVMS
QNX
VxWorks
Psion
Python has also been ported to the Java and .NET virtual machines
Getting Python
The most up-to-date and current source code, binaries, documentation, news, etc., is available on the official website of Python https://www.python.org/

You can download Python documentation from https://www.python.org/doc/. The documentation is available in HTML, PDF, and PostScript formats.

Installing Python
Python distribution is available for a wide variety of platforms. You need to download only the binary code applicable for your platform and install Python.

If the binary code for your platform is not available, you need a C compiler to compile the source code manually. Compiling the source code offers more flexibility in terms of choice of features that you require in your installation.

Here is a quick overview of installing Python on various platforms −

Unix and Linux Installation
Here are the simple steps to install Python on Unix/Linux machine.

Open a Web browser and go to https://www.python.org/downloads/.

Follow the link to download zipped source code available for Unix/Linux.

Download and extract files.

Editing the Modules/Setup file if you want to customize some options.

run ./configure script

make

make install

This installs Python at standard location /usr/local/bin and its libraries at /usr/local/lib/pythonXX where XX is the version of Python.

Windows Installation
Here are the steps to install Python on Windows machine.

Open a Web browser and go to https://www.python.org/downloads/.

Follow the link for the Windows installer python-XYZ.msi file where XYZ is the version you need to install.

To use this installer python-XYZ.msi, the Windows system must support Microsoft Installer 2.0. Save the installer file to your local machine and then run it to find out if your machine supports MSI.

Run the downloaded file. This brings up the Python install wizard, which is really easy to use. Just accept the default settings, wait until the install is finished, and you are done.

Macintosh Installation
Recent Macs come with Python installed, but it may be several years out of date. See http://www.python.org/download/mac/ for instructions on getting the current version along with extra tools to support development on the Mac. For older Mac OS's before Mac OS X 10.3 (released in 2003), MacPython is available.

Jack Jansen maintains it and you can have full access to the entire documentation at his website − http://www.cwi.nl/~jack/macpython.html. You can find complete installation details for Mac OS installation.

Setting up PATH
Programs and other executable files can be in many directories, so operating systems provide a search path that lists the directories that the OS searches for executables.

The path is stored in an environment variable, which is a named string maintained by the operating system. This variable contains information available to the command shell and other programs.

The path variable is named as PATH in Unix or Path in Windows (Unix is case sensitive; Windows is not).

In Mac OS, the installer handles the path details. To invoke the Python interpreter from any particular directory, you must add the Python directory to your path.

Setting path at Unix/Linux
To add the Python directory to the path for a particular session in Unix −

In the csh shell − type setenv PATH "$PATH:/usr/local/bin/python" and press Enter.

In the bash shell (Linux) − type export ATH="$PATH:/usr/local/bin/python" and press Enter.

In the sh or ksh shell − type PATH="$PATH:/usr/local/bin/python" and press Enter.

Note − /usr/local/bin/python is the path of the Python directory

Setting path at Windows
To add the Python directory to the path for a particular session in Windows −

At the command prompt − type path %path%;C:\Python and press Enter.

Note − C:\Python is the path of the Python directory

Python Environment Variables
Here are important environment variables, which can be recognized by Python −

Sr.No.	Variable & Description
1	
PYTHONPATH

It has a role similar to PATH. This variable tells the Python interpreter where to locate the module files imported into a program. It should include the Python source library directory and the directories containing Python source code. PYTHONPATH is sometimes preset by the Python installer.

2	
PYTHONSTARTUP

It contains the path of an initialization file containing Python source code. It is executed every time you start the interpreter. It is named as .pythonrc.py in Unix and it contains commands that load utilities or modify PYTHONPATH.

3	
PYTHONCASEOK

It is used in Windows to instruct Python to find the first case-insensitive match in an import statement. Set this variable to any value to activate it.

4	
PYTHONHOME

It is an alternative module search path. It is usually embedded in the PYTHONSTARTUP or PYTHONPATH directories to make switching module libraries easy.

Running Python
There are three different ways to start Python −

Interactive Interpreter
You can start Python from Unix, DOS, or any other system that provides you a command-line interpreter or shell window.

Enter python the command line.

Start coding right away in the interactive interpreter.

$python # Unix/Linux
or
python% # Unix/Linux
or
C:> python # Windows/DOS
Here is the list of all the available command line options −

Sr.No.	Option & Description
1	
-d

It provides debug output.

2	
-O

It generates optimized bytecode (resulting in .pyo files).

3	
-S

Do not run import site to look for Python paths on startup.

4	
-v

verbose output (detailed trace on import statements).

5	
-X

disable class-based built-in exceptions (just use strings); obsolete starting with version 1.6.

6	
-c cmd

run Python script sent in as cmd string

7	
file

run Python script from given file

Script from the Command-line
A Python script can be executed at command line by invoking the interpreter on your application, as in the following −

$python script.py # Unix/Linux

or

python% script.py # Unix/Linux

or 

C: >python script.py # Windows/DOS
Note − Be sure the file permission mode allows execution.

Integrated Development Environment
You can run Python from a Graphical User Interface (GUI) environment as well, if you have a GUI application on your system that supports Python.

Unix − IDLE is the very first Unix IDE for Python.

Windows − PythonWin is the first Windows interface for Python and is an IDE with a GUI.

Macintosh − The Macintosh version of Python along with the IDLE IDE is available from the main website, downloadable as either MacBinary or BinHex'd files.

If you are not able to set up the environment properly, then you can take help from your system admin. Make sure the Python environment is properly set up and working perfectly fine.

Note − All the examples given in subsequent chapters are executed with Python 2.4.3 version available on CentOS flavor of Linux.

We already have set up Python Programming environment online, so that you can execute all the available examples online at the same time when you are learning theory. Feel free to modify any example and execute it online.

"""



