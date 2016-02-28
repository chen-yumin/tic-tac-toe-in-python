# Import the GUI library Tkinter
import tkinter
# Import the messagebox module explicitly
from tkinter import messagebox

# Constants 
c_window_width = 640;
c_window_height = 480;
c_color_blue_light = "#e4f1fe";
c_color_blue_dark = "#304e62";
c_color_blue = "#a8d4f2";

# Create a Tkinter object
root = tkinter.Tk();

# Set window title
root.title("Tic Tac Toe");

try:
	# Set window icon
	root.iconbitmap('res/icon.ico');
except:	
	# An error has been caught when setting the icon
	tkinter.messagebox.showerror("Error", "Can't set the window icon.");

# Create a canvas with the desired size and color
canvas = tkinter.Canvas(root, bg=c_color_blue_light, height=c_window_height, width=c_window_width);

# Create a blue arch at the top of the canvas
arc = canvas.create_arc((-64, -368, c_window_width + 64, 192), start=0, extent=-180, fill=c_color_blue, outline="");

try:
	# From the image file create a PhotoImage object 
	logo_file = tkinter.PhotoImage(file="res/icon.png");
	# Create the logo image at the center of the canvas
	logo = canvas.create_image((c_window_width/2, c_window_height/2 - 96), image=logo_file);
except:	
	# An error has been caught when creating the logo image
	tkinter.messagebox.showerror("Error", "Can't create the logo image.\nPlease make sure the res folder is in the same directory as this script.");

# Pack the canvas
canvas.pack();

# Main loop
root.mainloop();