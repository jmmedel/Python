


"""


Python Forensics - Python Imaging Library

Extracting valuable information from the resources available is a vital part of digital forensics. Getting access to all the information available is essential for an investigation process 
as it helps in retrieving appropriate evidence.

Resources that contain data can be either simple data structures such as databases or complex data structures such as a JPEG image. Simple data structures can be easily accessed using simple desktop tools, while extracting information from complex data structures require sophisticated programming tools.

Python Imaging Library
The Python Imaging Library (PIL) adds image processing capabilities to your Python interpreter. This library supports many file formats, and provides powerful image processing and graphics capabilities. You can download the source files of PIL from: 

The following illustration shows the complete flow diagram of extracting data from images (complex data structures) in PIL.

Example
Now, let’s have a programming example to understand how it actually works.

Step 1 − Suppose we have the following image from where we need to extract information.

Python Imaging Library Step1
Step 2 − When we open this image using PIL, it will first note the necessary points required for extracting evidence, which includes various pixel values. Here is the code to open the image and record its pixel values −

from PIL import Image

"""

from PIL import Image
im = Image.open('Capture.jpeg', 'r')
pix_val = list(im.getdata())
pix_val_flat = [x for sets in pix_val for x in sets]
print (pix_val_flat)

