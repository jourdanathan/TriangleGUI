import tkinter as tk
from tkinter import messagebox, PhotoImage


# Callback function to check triangle type based on entered angles
def check_triangle_type():
    try:
        # Get angles and convert them to float
        angle1 = float(entry_angle1.get())
        angle2 = float(entry_angle2.get())
        angle3 = float(entry_angle3.get())

        # Check if the sum of angles is 180 degrees
        if angle1 + angle2 + angle3 != 180:
            raise ValueError("The sum of the angles must be 180 degrees.")

        # Determine triangle type and update image accordingly
        if angle1 == 90 or angle2 == 90 or angle3 == 90:
            triangle_type = "Right"
            image_label.config(image=right_triangle_img)
        elif angle1 < 90 and angle2 < 90 and angle3 < 90:
            triangle_type = "Acute"
            image_label.config(image=acute_triangle_img)
        else:
            triangle_type = "Obtuse"
            image_label.config(image=obtuse_triangle_img)

        # Display triangle type
        label_result.config(text=f"Triangle Type: {triangle_type}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))


# Callback function to clear angle entries and result
def clear_entries():
    entry_angle1.delete(0, tk.END)
    entry_angle2.delete(0, tk.END)
    entry_angle3.delete(0, tk.END)
    label_result.config(text="Triangle Type:")
    image_label.config(image=blank_img)


# Callback function to exit the application
def exit_application():
    root.destroy()


# Initialize main window
root = tk.Tk()
root.title("Triangle Type Checker")

# Main frame
frame_main = tk.Frame(root)
frame_main.pack()

# Title label
label_title = tk.Label(frame_main, text="Triangle Type Checker")
label_title.pack()

# Input frame
frame_inputs = tk.Frame(frame_main)
frame_inputs.pack()

# Angle input labels and entries
label_angle1 = tk.Label(frame_inputs, text="Angle 1:")
label_angle1.grid(row=0, column=0)
entry_angle1 = tk.Entry(frame_inputs)
entry_angle1.grid(row=0, column=1)

label_angle2 = tk.Label(frame_inputs, text="Angle 2:")
label_angle2.grid(row=1, column=0)
entry_angle2 = tk.Entry(frame_inputs)
entry_angle2.grid(row=1, column=1)

label_angle3 = tk.Label(frame_inputs, text="Angle 3:")
label_angle3.grid(row=2, column=0)
entry_angle3 = tk.Entry(frame_inputs)
entry_angle3.grid(row=2, column=1)

# Result label
label_result = tk.Label(frame_main, text="Triangle Type:")
label_result.pack()

# Image setup
blank_img = PhotoImage(file="blank.png")
acute_triangle_img = PhotoImage(file="acute_triangle.png")
right_triangle_img = PhotoImage(file="right_triangle.png")
obtuse_triangle_img = PhotoImage(file="obtuse_triangle.png")

# Image label
image_label = tk.Label(frame_main, image=blank_img)
image_label.pack()

# Button frame
frame_buttons = tk.Frame(frame_main)
frame_buttons.pack()

# Check, clear, and exit buttons
button_check = tk.Button(frame_buttons, text="Check", command=check_triangle_type)
button_check.grid(row=0, column=0)

button_clear = tk.Button(frame_buttons, text="Clear", command=clear_entries)
button_clear.grid(row=0, column=1)

button_exit = tk.Button(frame_buttons, text="Exit", command=exit_application)
button_exit.grid(row=0, column=2)

root.mainloop()

