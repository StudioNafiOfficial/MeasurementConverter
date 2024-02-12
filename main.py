import tkinter as tk
import ttkbootstrap as ttk

# functions


def convert():
    print(entryStr.get())

# window
window = ttk.Window(themename="vapor")
window.title("Measurement Converter")
window.geometry("500x500")

# Body title
titleLabel = ttk.Label(master=window,
                        text="Measurement Converter",
                        font="Calibri 30 bold italic")
titleLabel.pack()


# input
# input field
inputFrame = ttk.Frame(master=window)
entryStr = tk.StringVar()
entry = ttk.Entry(master=inputFrame,
                 textvariable=entryStr)
button = ttk.Button(master=inputFrame,
                   text="Convert",
                   command=convert)
entry.pack(side="left", padx=10)
button.pack(side="left")
inputFrame.pack(pady=20)

# input dropdown
selectedOption = tk.StringVar()
options = ["Meters", "Yards", "Feet", 
           "Inches", "Centimeters","Milimeters"]
dropdown = ttk.OptionMenu(window, 
                          selectedOption,
                          "Select a measurement",
                          *options)
dropdown.pack()

# output



# run
window.mainloop()