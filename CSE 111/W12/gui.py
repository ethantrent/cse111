"""Your program must include a GUI that opens when you run your program.
The GUI must allow a user to enter input.
When the user enters valid input, your program must compute correct results and display those results in the GUI.

Volume of a tire: v = πw2awa + 2,540d/10,000,000,000"""

import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import FloatEntry, IntEntry
import math


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root) # Create a frame (window) widget.
    frm_main.master.title("Tire Volume Calculator") # Set the title of the window.
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1) # Pack the frame into the root widget.    

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and
# each widget is an object, the code to make a GUI usually has many
# variables to store the many objects. Because there are so many
# variable names, programmers often adopt a naming convention to help
# a programmer keep track of all the variables. One popular naming
# convention is to type a three letter prefix in front of the names
# of all variables that store GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Width (mm):"
    lbl_width = Label(frm_main, text="Width (mm):")
    # Create an integer entry box where a user will enter the width of the tire in mm
    ent_width = IntEntry(frm_main, width=4, lower_bound=0, upper_bound=1000)
    # Create a label that displays "mm"
    lbl_width_units = Label(frm_main, text="mm")

    # Create a label that displays "Aspect Ratio (%):"
    lbl_aspect = Label(frm_main, text="Aspect Ratio (%):")
    # Create an integer entry box where a user will enter the aspect ratio of the tire
    ent_aspect = IntEntry(frm_main, width=4, lower_bound=0, upper_bound=100)
    # Create a label that displays "%"
    lbl_aspect_units = Label(frm_main, text="%")

    # Create a label that displays "Diameter (in):"
    lbl_diameter = Label(frm_main, text="Diameter (in):")
    # Create an integer entry box where a user will enter the diameter of the tire in inches
    ent_diameter = FloatEntry(frm_main, width=4, lower_bound=0, upper_bound=100)
    # Create a label that displays "in"
    lbl_diameter_units = Label(frm_main, text="in")

    # Create a label that displays "Volume:"
    lbl_volume = Label(frm_main, width=10)
    # Create a label that displays "liters"
    lbl_volume_units = Label(frm_main, text="liters")

    # Create the Clear button
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the widgets in a grid
    lbl_width.grid(row=0, column=0, padx=3, pady=3)
    ent_width.grid(row=0, column=1, padx=3, pady=3)
    lbl_width_units.grid(row=0, column=2, padx=0, pady=3)

    lbl_aspect.grid(row=1, column=0, padx=3, pady=3)
    ent_aspect.grid(row=1, column=1, padx=3, pady=3)
    lbl_aspect_units.grid(row=1, column=2, padx=0, pady=3)

    lbl_diameter.grid(row=2, column=0, padx=3, pady=3)
    ent_diameter.grid(row=2, column=1, padx=3, pady=3)
    lbl_diameter_units.grid(row=2, column=2, padx=0, pady=3)

    lbl_volume.grid(row=3, column=1, padx=3, pady=3)
    lbl_volume_units.grid(row=3, column=2, padx=0, pady=3)

    btn_clear.grid(row=4, column=0, padx=3, pady=3, columnspan=3, sticky="w")

    def calculate(event):
        """Compute and display the tire volume."""
        try:
            # Get the user's inputs
            width = ent_width.get()
            aspect = ent_aspect.get()
            diameter = ent_diameter.get()

            # Calculate tire volume using the formula
            # v = πw2awa + 2,540d/10,000,000,000
            volume = (math.pi * width**2 * aspect * (width * aspect + 2540 * diameter)) / 10000000000

            # Display the volume
            lbl_volume.config(text=f"{volume:.2f}")

        except ValueError:
            # When the user deletes all the digits in any entry box,
            # clear the volume label
            lbl_volume.config(text="")

    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_width.clear()
        ent_aspect.clear()
        ent_diameter.clear()
        lbl_volume.config(text="")
        ent_width.focus()

    # Bind the calculate function to all entry boxes
    ent_width.bind("<KeyRelease>", calculate)
    ent_aspect.bind("<KeyRelease>", calculate)
    ent_diameter.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button
    btn_clear.config(command=clear)

    # Give the keyboard focus to the width entry box
    ent_width.focus()


# If this file is executed like this:
# > python gui.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
