import tkinter as tk


def run():
    # Create the main window
    root = tk.Tk()
    root.title("Tkinter Demo")

    # Create a label widget with the text "Hello, World!"
    label = tk.Label(root, text="Hello, World!", padx=200, pady=200)

    # Add the label to the window
    label.pack()

    # Start the Tkinter event loop
    root.mainloop()
