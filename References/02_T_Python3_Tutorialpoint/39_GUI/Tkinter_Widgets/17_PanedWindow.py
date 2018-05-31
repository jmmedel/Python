


"""

Python 3 - Tkinter PanedWindow

A PanedWindow is a container widget that may contain any number of panes, arranged horizontally or vertically.

Each pane contains one widget and each pair of panes is separated by a moveable (via mouse movements) sash. Moving a sash causes the widgets on either side of the sash to be resized.

Syntax
Here is the simple syntax to create this widget −

w = PanedWindow( master, option, ... )
Parameters
master − This represents the parent window.

options − Here is the list of most commonly used options for this widget. These options can be used as key-value pairs separated by commas.

S.No.	Option & Description
1	
bg

The color of the slider and arrowheads when the mouse is not over them.

2	
bd

The width of the 3-d borders around the entire perimeter of the trough, and also the width of the 3-d effects on the arrowheads and slider. Default is no border around the trough, and a 2-pixel border around the arrowheads and slider.

3	
borderwidth

Default is 2.

4	
cursor

The cursor that appears when the mouse is over the window.

5	
handlepad

Default is 8.

6	
handlesize

Default is 8.

9	
height

No default value.

10	
orient

Default is HORIZONTAL.

11	
relief

Default is FLAT.

12	
sashcursor

No default value.

13	
sashrelief

Default is RAISED.

14	
sashwidth

Default is 2.

15	
showhandle

No default value

16	
width

No default value.

Methods
PanedWindow objects have these methods −

S.No.	Method & Description
1	
add(child, options)

Adds a child window to the paned window.

2	
get(startindex [,endindex])

This method returns a specific character or a range of text.

3	
config(options)

Modifies one or more widget options. If no options are given, the method returns a dictionary containing all current option values.

Example
Try the following example yourself. Here's how to create a 3-pane widget −

"""
