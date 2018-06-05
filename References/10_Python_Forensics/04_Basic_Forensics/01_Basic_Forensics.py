


"""

Python Forensics - Basic Forensic Application

For creating an application as per the Forensic guidelines, it is important to understand and follow its naming conventions and patterns.

Naming Conventions
During the development of Python forensics applications, the rules and conventions to be followed are described in the following table.

Naming Convention	Example
Constants	Uppercase with underscore separation	HIGH_TEMPERATURE
Local variable name	Lowercase with bumpy caps (underscores are optional)	currentTemperature
Global variable name	Prefix gl lowercase with bumpy caps (underscores are optional)	gl_maximumRecordedTemperature
Functions name	Uppercase with bumpy caps (underscores optional) with active voice	ConvertFarenheitToCentigrade(...)
Object name	Prefix ob_ lowercase with bumpy caps	ob_myTempRecorder
Module	An underscore followed by lowercase with bumpy caps	_tempRecorder
Class names	Prefix class_ then bumpy caps and keep brief	class_TempSystem
Let us take a scenario to understand the importance of naming conventions in Computational Forensics. Suppose we have a hashing algorithm that is normally used for encrypting data. The one-way hashing algorithm takes input as a stream of binary data; this could be a password, a file, binary data, or any digital data. The hashing algorithm then produces a message digest (md) with respect to the data received in the input.

It is practically impossible to create a new binary input that will generate a given message digest. Even a single bit of the binary input data, if changed, will generate a unique message, which is different than the previous one.

Example
Take a look at the following sample program which follows the above-mentioned conventions.


"""

import sys, md5   # necessary libraries
print ("Please enter your full name")
line = sys.stdin.readline()
line = line.rstrip()
md5_object = md5.new()
md5_object.update(line)
print (md5_object.hexdigest())   # Prints the output as per the hashing algorithm i.e. md5


"""

In this program, the Python script accepts the input (your full name) and converts it as per the md5 hashing algorithm. It encrypts the data and secures the information, if required. As per forensic guidelines, the name of evidences or any other proofs can be secured in this pattern.


"""

