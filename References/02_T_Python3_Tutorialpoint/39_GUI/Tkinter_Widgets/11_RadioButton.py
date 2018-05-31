


"""


Python 3 - Tkinter Radiobutton


This widget implements a multiple-choice button, which is a way to offer many possible selections to the user and lets user choose only one of them.

In order to implement this functionality, each group of radiobuttons must be associated to the same variable and each one of the buttons must symbolize a single value. You can use the Tab key to switch from one radionbutton to another.

Syntax
Here is the simple syntax to create this widget −

w = Radiobutton ( master, option, ...  )
Parameters
master − This represents the parent window.

options − Here is the list of most commonly used options for this widget. These options can be used as key-value pairs separated by commas.

S.No.	Option & Description
1	
activebackground

The background color when the mouse is over the radiobutton.

2	
activeforeground

The foreground color when the mouse is over the radiobutton.

3	
anchor

If the widget inhabits a space larger than it needs, this option specifies where the radiobutton will sit in that space. The default is anchor = CENTER.

4	
bg

The normal background color behind the indicator and label.

5	
bitmap

To display a monochrome image on a radiobutton, set this option to a bitmap.

6	
borderwidth

The size of the border around the indicator part itself. Default is 2 pixels.

7	
command

A procedure to be called every time the user changes the state of this radiobutton.

8	
cursor

If you set this option to a cursor name (arrow, dot etc.), the mouse cursor will change to that pattern when it is over the radiobutton.

9	
font

The font used for the text.

10	
fg

The color used to render the text.

11	
height

The number of lines (not pixels) of text on the radiobutton. Default is 1.

12	
highlightbackground

The color of the focus highlight when the radiobutton does not have focus.

13	
highlightcolor

The color of the focus highlight when the radiobutton has the focus.

14	
image

To display a graphic image instead of text for this radiobutton, set this option to an image object.

15	
justify

If the text contains multiple lines, this option controls how the text is justified: CENTER (the default), LEFT, or RIGHT.

16	
padx

How much space to leave to the left and right of the radiobutton and text. Default is 1.

17	
pady

How much space to leave above and below the radiobutton and text. Default is 1.

18	
relief

Specifies the appearance of a decorative border around the label. The default is FLAT; for other values.

19	
selectcolor

The color of the radiobutton when it is set. Default is red.

20	
selectimage

If you are using the image option to display a graphic instead of text when the radiobutton is cleared, you can set the selectimage option to a different image that will be displayed when the radiobutton is set.

21	
state

The default is state = NORMAL, but you can set state = DISABLED to gray out the control and make it unresponsive. If the cursor is currently over the radiobutton, the state is ACTIVE.

22	
text

The label displayed next to the radiobutton. Use newlines ("\n") to display multiple lines of text.

23	
textvariable

To slave the text displayed in a label widget to a control variable of class StringVar, set this option to that variable.

24	
underline

You can display an underline (_) below the nth letter of the text, counting from 0, by setting this option to n. The default is underline = -1, which means no underlining.

25	
value

When a radiobutton is turned on by the user, its control variable is set to its current value option. If the control variable is an IntVar, give each radiobutton in the group a different integer value option. If the control variable is a StringVar, give each radiobutton a different string value option.

26	
variable

The control variable that this radiobutton shares with the other radiobuttons in the group. This can be either an IntVar or a StringVar.

27	
width

Width of the label in characters (not pixels!). If this option is not set, the label will be sized to fit its contents.

28	
wraplength

You can limit the number of characters in each line by setting this option to the desired number. The default value, 0, means that lines will be broken only at newlines.

Methods
S.No.	Method & Description
1	
deselect()

Clears (turns off) the radiobutton.

2	
flash()

Flashes the radiobutton a few times between its active and normal colors, but leaves it the way it started.

3	
invoke()

You can call this method to get the same actions that would occur if the user clicked on the radiobutton to change its state.

4	
select()

Sets (turns on) the radiobutton.


"""


from tkinter import *

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

root = Tk()
var = IntVar()
R1 = Radiobutton(root, text = "Option 1", variable = var, value = 1,
                  command = sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text = "Option 2", variable = var, value = 2,
                  command = sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text = "Option 3", variable = var, value = 3,
                  command = sel)
R3.pack( anchor = W)

label = Label(root)
label.pack()
root.mainloop()





