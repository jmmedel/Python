


"""

Python 3 - Tkinter Scrollbar
Advertisements
 Previous Page Next Page  
This widget provides a slide controller that is used to implement vertical scrolled widgets, such as Listbox, Text and Canvas. Note that you can also create horizontal scrollbars on Entry widgets.

Syntax
Here is the simple syntax to create this widget −

 w = Scrollbar ( master, option, ... )
Parameters
master − This represents the parent window.

options − Here is the list of most commonly used options for this widget. These options can be used as key-value pairs separated by commas.

S.No.	Option & Description
1	
activebackground

The color of the slider and arrowheads when the mouse is over them.

2	
bg

The color of the slider and arrowheads when the mouse is not over them.

3	
bd

The width of the 3-d borders around the entire perimeter of the trough, and also the width of the 3-d effects on the arrowheads and slider. Default is no border around the trough, and a 2-pixel border around the arrowheads and slider.

4	
command

A procedure to be called whenever the scrollbar is moved.

5	
cursor

The cursor that appears when the mouse is over the scrollbar.

6	
elementborderwidth

The width of the borders around the arrowheads and slider. The default is elementborderwidth = -1, which means to use the value of the borderwidth option.

7	
highlightbackground

The color of the focus highlight when the scrollbar does not have focus.

8	
highlightcolor

The color of the focus highlight when the scrollbar has the focus.

9	
highlightthickness

The thickness of the focus highlight. Default is 1. Set to 0 to suppress display of the focus highlight.

10	
jump

This option controls what happens when a user drags the slider. Normally (jump = 0), every small drag of the slider causes the command callback to be called. If you set this option to 1, the callback isn't called until the user releases the mouse button.

11	
orient

Set orient = HORIZONTAL for a horizontal scrollbar, orient = VERTICAL for a vertical one.

12	
repeatdelay

This option controls how long button 1 has to be held down in the trough before the slider starts moving in that direction repeatedly. Default is repeatdelay = 300, and the units are milliseconds.

13	
repeatinterval

repeatinterval

14	
takefocus

Normally, you can tab the focus through a scrollbar widget. Set takefocus = 0 if you don't want this behavior.

15	
troughcolor

The color of the trough.

16	
width

Width of the scrollbar (its y dimension if horizontal, and its x dimension if vertical). Default is 16.

Methods
Scrollbar objects have these methods −

S.No.	Method & Description
1	
get()

Returns two numbers (a, b) describing the current position of the slider. The a value gives the position of the left or top edge of the slider, for horizontal and vertical scrollbars respectively; the b value gives the position of the right or bottom edge.

2	
set ( first, last )

To connect a scrollbar to another widget w, set w's xscrollcommand or yscrollcommand to the scrollbar's set() method. The arguments have the same meaning as the values returned by the get() method.



"""


from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

mainloop()

