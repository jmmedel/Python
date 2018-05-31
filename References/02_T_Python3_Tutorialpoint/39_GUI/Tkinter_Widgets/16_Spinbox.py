


"""


Python 3 - Tkinter Spinbox


The Spinbox widget is a variant of the standard Tkinter Entry widget, which can be used to select from a fixed number of values.

Syntax
Here is the simple syntax to create this widget −

w = Spinbox( master, option, ... )
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
disabledbackground

The background color to use when the widget is disabled.

7	
disabledforeground

The text color to use when the widget is disabled.

8	
fg

Text color.

9	
font

The font to use in this widget.

10	
format

Format string. No default value.

11	
from_

The minimum value. Used together with to to limit the spinbox range.

12	
justify

Default is LEFT

13	
relief

Default is SUNKEN.

14	
repeatdelay

Together with repeatinterval, this option controls button auto-repeat. Both values are given in milliseconds.

15	
repeatinterval

See repeatdelay.

16	
state

One of NORMAL, DISABLED, or "readonly". Default is NORMAL.

17	
textvariable

No default value.

18	
to

See from.

19	
validate

Validation mode. Default is NONE.

20	
validatecommand

Validation callback. No default value.

21	
values

A tuple containing valid values for this widget. Overrides from/to/increment.

22	
vcmd

Same as validatecommand.

23	
width

Widget width, in character units. Default is 20.

24	
wrap

If true, the up and down buttons will wrap around.

25	
xscrollcommand

Used to connect a spinbox field to a horizontal scrollbar. This option should be set to the set method of the corresponding scrollbar.

Methods
Spinbox objects have these methods −

S.No.	Methods and Description
1	
delete(startindex [,endindex])

This method deletes a specific character or a range of text.

2	
get(startindex [,endindex])

This method returns a specific character or a range of text.

3	
identify(x, y)

Identifies the widget element at the given location.

4	
index(index)

Returns the absolute value of an index based on the given index.

5	
insert(index [,string]...)

This method inserts strings at the specified index location.

6	
invoke(element)

Invokes a spinbox button.

"""


from tkinter import *

master = Tk()

w = Spinbox(master, from_ = 0, to = 10)
w.pack()

mainloop()



