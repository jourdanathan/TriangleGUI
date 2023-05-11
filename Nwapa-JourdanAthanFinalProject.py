import tkinter as tk
from tkinter import messagebox, PhotoImage

# Callback function to open the main application window
def open_main_window():
    title_window.destroy()  # Close the title window

    # Callback function to check triangle type based on entered angles
    def check_triangle_type():
        try:
            angle1 = entry_angle1.get()  # Get angle 1 value from input
            angle2 = entry_angle2.get()  # Get angle 2 value from input
            angle3 = entry_angle3.get()  # Get angle 3 value from input

            # Check if any of the input fields are empty
            if not angle1 or not angle2 or not angle3:
                raise ValueError("Please ensure all fields are filled in.")

            angle1 = float(angle1)  # Convert angle 1 value to float
            angle2 = float(angle2)  # Convert angle 2 value to float
            angle3 = float(angle3)  # Convert angle 3 value to float

            # Check if the sum of angles is 180 degrees
            if angle1 + angle2 + angle3 != 180:
                raise ValueError("The sum of the angles must be 180 degrees.")

            # Determine triangle type and update image accordingly
            if angle1 == 90 or angle2 == 90 or angle3 == 90:
                triangle_type = "Right"  # Right-angled triangle
                image_label.config(image=right_triangle_img)
            elif angle1 < 90 and angle2 < 90 and angle3 < 90:
                triangle_type = "Acute"  # Acute triangle
                image_label.config(image=acute_triangle_img)
            else:
                triangle_type = "Obtuse"  # Obtuse triangle
                image_label.config(image=obtuse_triangle_img)

            # Display triangle type
            label_result.config(text=f"Triangle Type: {triangle_type}")

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    # Callback function to clear angle entries and result
    def clear_entries():
        entry_angle1.delete(0, tk.END)  # Clear angle 1 entry
        entry_angle2.delete(0, tk.END)  # Clear angle 2 entry
        entry_angle3.delete(0, tk.END)  # Clear angle 3 entry
        label_result.config(text="Triangle Type:")  # Reset result label
        image_label.config(image=blank_img)  # Reset image label

    # Callback function to exit the application
    def exit_application():
        main_window.destroy()  # Close the main window and exit the application

    # Initialize main window
    main_window = tk.Tk()
    main_window.title("Triangle Type Checker")

    # Main frame
    frame_main = tk.Frame(main_window)  # Create main frame
    frame_main.pack()  # Add main frame to the window

    # Title label
    label_title = tk.Label(frame_main, text="Triangle Type Checker")  # Create title label
    label_title.pack()  # Add title label to the main frame

    # Input frame
    frame_inputs = tk.Frame(frame_main)  # Create input frame
    frame_inputs.pack()  # Add input frame to the main frame

    # Angle input labels and entries
    label_angle1 = tk.Label(frame_inputs, text="Angle 1:")  # Create angle 1 label
    label_angle1.grid(row=0, column=0)  # Add angle 1 label to the input frame
   
    entry_angle1 = tk.Entry(frame_inputs)  # Create angle 1 entry
    entry_angle1.grid(row=0, column=1)  # Add angle 1 entry to the input frame

    label_angle2 = tk.Label(frame_inputs, text="Angle 2:")  # Create angle 2 label
    label_angle2.grid(row=1, column=0)  # Add angle 2 label to the input frame
    entry_angle2 = tk.Entry(frame_inputs)  # Create angle 2 entry
    entry_angle2.grid(row=1, column=1)  # Add angle 2 entry to the input frame

    label_angle3 = tk.Label(frame_inputs, text="Angle 3:")  # Create angle 3 label
    label_angle3.grid(row=2, column=0)  # Add angle 3 label to the input frame
    entry_angle3 = tk.Entry(frame_inputs)  # Create angle 3 entry
    entry_angle3.grid(row=2, column=1)  # Add angle 3 entry to the input frame

    # Result label
    label_result = tk.Label(frame_main, text="Triangle Type:")  # Create result label
    label_result.pack()  # Add result label to the main frame

    # Image resources
    blank_img = PhotoImage(file="blank.png")
    acute_triangle_img = PhotoImage(file="acute_triangle.png")
    right_triangle_img = PhotoImage(file="right_triangle.png")
    obtuse_triangle_img = PhotoImage(file="obtuse_triangle.png")

    # Image label
    image_label = tk.Label(frame_main, image=blank_img)  # Create image label
    image_label.pack()  # Add image label to the main frame

    # Buttons frame
    frame_buttons = tk.Frame(frame_main)  # Create buttons frame
    frame_buttons.pack()  # Add buttons frame to the main frame

    # Button: Check
    button_check = tk.Button(frame_buttons, text="Check", command=check_triangle_type)
    button_check.grid(row=0, column=0)  # Add "Check" button to the buttons frame

    # Button: Clear
    button_clear = tk.Button(frame_buttons, text="Clear", command=clear_entries)
    button_clear.grid(row=0, column=1)  # Add "Clear" button to the buttons frame

    # Button: Exit
    button_exit = tk.Button(frame_buttons, text="Exit", command=exit_application)
    button_exit.grid(row=0, column=2)  # Add "Exit" button to the buttons frame

    main_window.mainloop()

# Title window
title_window = tk.Tk()
title_window.title("Welcome")

# Title frame
frame_title = tk.Frame(title_window)  # Create title frame
frame_title.pack()  # Add title frame to the title window

# Welcome label
label_welcome = tk.Label(frame_title, text="Welcome to the Triangle Type Checker!")
label_welcome.pack()  # Add welcome label to the title frame

# Start button
button_start = tk.Button(frame_title, text="Start", command=open_main_window)
button_start.pack()  # Add "Start" button to the title frame

title_window.mainloop()
