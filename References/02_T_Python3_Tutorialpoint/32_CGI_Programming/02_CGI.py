

"""

Hello Word! This is my first CGI program
This hello.py script is a simple Python script, which writes its output on STDOUT file, i.e., screen. There is one important and extra feature available which is first line to be printed Content-type:text/html\r\n\r\n. This line is sent back to the browser and it specifies the content type to be displayed on the browser screen.

By now you must have understood basic concept of CGI and you can write many complicated CGI programs using Python. This script can interact with any other external system also to exchange information such as RDBMS.

HTTP Header
The line Content-type:text/html\r\n\r\n is part of HTTP header which is sent to the browser to understand the content. All the HTTP header will be in the following form −

HTTP Field Name: Field Content

For Example
Content-type: text/html\r\n\r\n
There are few other important HTTP headers, which you will use frequently in your CGI Programming.

Sr.No.	Header & Description
1	
Content-type:

A MIME string defining the format of the file being returned. Example is Content-type:text/html

2	
Expires: Date

The date the information becomes invalid. It is used by the browser to decide when a page needs to be refreshed. A valid date string is in the format 01 Jan 1998 12:00:00 GMT.

3	
Location: URL

The URL that is returned instead of the URL requested. You can use this field to redirect a request to any file.

4	
Last-modified: Date

The date of last modification of the resource.

5	
Content-length: N

The length, in bytes, of the data being returned. The browser uses this value to report the estimated download time for a file.

6	
Set-Cookie: String

Set the cookie passed through the string

CGI Environment Variables
All the CGI programs have access to the following environment variables. These variables play an important role while writing any CGI program.

Sr.No.	Variable Name & Description
1	
CONTENT_TYPE

The data type of the content. Used when the client is sending attached content to the server. For example, file upload.

2	
CONTENT_LENGTH

The length of the query information. It is available only for POST requests.

3	
HTTP_COOKIE

Returns the set cookies in the form of key & value pair.

4	
HTTP_USER_AGENT

The User-Agent request-header field contains information about the user agent originating the request. It is name of the web browser.

5	
PATH_INFO

The path for the CGI script.

6	
QUERY_STRING

The URL-encoded information that is sent with GET method request.

7	
REMOTE_ADDR

The IP address of the remote host making the request. This is useful logging or for authentication.

8	
REMOTE_HOST

The fully qualified name of the host making the request. If this information is not available, then REMOTE_ADDR can be used to get IR address.

9	
REQUEST_METHOD

The method used to make the request. The most common methods are GET and POST.

10	
SCRIPT_FILENAME

The full path to the CGI script.

11	
SCRIPT_NAME

The name of the CGI script.

12	
SERVER_NAME

The server's hostname or IP Address

13	
SERVER_SOFTWARE

The name and version of the software the server is running.

Here is small CGI program to list out all the CGI variables. Click this link to see the result Get Environment


"""

import os

print "Content-type: text/html\r\n\r\n";
print "<font size=+1>Environment</font><\br>";
for param in os.environ.keys():
   print "<b>%20s</b>: %s<\br>" % (param, os.environ[param])
   

