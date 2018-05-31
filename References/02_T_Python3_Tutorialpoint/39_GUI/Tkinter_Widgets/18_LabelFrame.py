


"""

Python 3 - Tkinter LabelFrame

A labelframe is a simple container widget. Its primary purpose is to act as a spacer or container for complex window layouts.

This widget has the features of a frame plus the ability to display a label.

Syntax
Here is the simple syntax to create this widget −

w = LabelFrame( master, option, ... )
Parameters
master − This represents the parent window.

options − Here is the list of most commonly used options for this widget. These options can be used as key-value pairs separated by commas.

S.No.	Option & Description
1	
bg

The normal background color displayed behind the label and indicator.

2	
bd

The size of the border around the indicator. Default is 2 pixels.

3	
cursor

If you set this option to a cursor name (arrow, dot etc.), the mouse cursor will change to that pattern when it is over the checkbutton.

4	
font

The vertical dimension of the new frame.

5	
height

The vertical dimension of the new frame.

6	
labelAnchor

Specifies where to place the label.

7	
highlightbackground

Color of the focus highlight when the frame does not have focus.

8	
highlightcolor

Color shown in the focus highlight when the frame has the focus.

9	
highlightthickness

Thickness of the focus highlight.

10	
relief

With the default value, relief = FLAT, the checkbutton does not stand out from its background. You may set this option to any of the other styles

11	
text

Specifies a string to be displayed inside the widget.

12	
width

Specifies the desired width for the window.

Example
Try the following example yourself. Here is how to create a labelframe widget −


"""


from tkinter import *

root = Tk()

labelframe = LabelFrame(root, text = "This is a LabelFrame")
labelframe.pack(fill = "both", expand = "yes")
 
left = Label(labelframe, text = "Inside the LabelFrame")
left.pack()
 
root.mainloop()
