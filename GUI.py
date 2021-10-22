# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
from tkinter import *
from tkinter import ttk

# import filedialog module
from tkinter import filedialog
import tkinter

# Function for opening the
# file explorer window
window = Tk()
label_file_explorer = Label(window,
                            text="File Explorer using Tkinter",
                            width=100, height=4,
                            fg="blue")

filename = ""
date = ""
n1 = tkinter.StringVar()
datechoosen = ttk.Combobox(window, width=27,
                           textvariable=n1)
n2 = tkinter.StringVar()
monthchoosen = ttk.Combobox(window, width=27,
                            textvariable=n2)
n3 = tkinter.StringVar()
yearchoosen = ttk.Combobox(window, width=27,
                           textvariable=n3)


def browseFiles():
    filename = filedialog.askopenfilename(initialdir="C:/example",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))

    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)


def submit():
    print("Submit button clicked")
    d = datechoosen.get()
    m = monthchoosen.get()
    y = yearchoosen.get()
    date = "d" + d+m+y
    # return(date)


def frame():
    # Create the root window
    # window = Tk()

    # Set window title
    window.title('File Explorer')

# Set window size
    window.geometry("500x500")

# Set window background color
    window.config(background="white")

# Create a File Explorer label
    # label_file_explorer = Label(window,
    #                       text="File Explorer using Tkinter",
    #                      width=100, height=4,
    #                     fg="blue")

    button_explore = Button(window,
                            text="Browse Files",
                            command=browseFiles)

    button_submit = Button(window,
                           text="Submit",
                           command=submit)

    button_exit = Button(window,
                         text="Exit",
                         command=exit)

    # if (filename != '' and date != ''):
    #   print(filename)
    #  print(date)
    # return(filename,date)
# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
    label_file_explorer.grid(column=1, row=1)

    button_explore.grid(column=1, row=2)

    button_submit.grid(column=1, row=24)
    ttk.Label(window, text="Select the Date :",
              font=("Times New Roman", 10)).grid(column=0,
                                                 row=15, padx=10, pady=25)

    button_exit.grid(column=1, row=27)
    ttk.Label(window, text="Select the Date :",
              font=("Times New Roman", 10)).grid(column=0,
                                                 row=16, padx=10, pady=25)

    #n = tkinter.StringVar()
    # datechoosen = ttk.Combobox(window, width=27,
    #                       textvariable=n)

# Adding combobox drop down list
    datechoosen['values'] = ('01',
                             '02',
                             '03',
                             '04',
                             '05',
                             '06',
                             '07',
                             '08',
                             '09',
                             '10',
                             '11',
                             '12',
                             '13',
                             '14',
                             '15',
                             '16',
                             '17',
                             '18',
                             '19',
                             '20',
                             '21',
                             '22',
                             '23',
                             '24',
                             '25',
                             '26',
                             '27',
                             '28',
                             '29',
                             '30',
                             '31')

    datechoosen.grid(column=1, row=15)

# Shows february as a default value
    datechoosen.current(1)

#window = tkinter.Tk()
# window.geometry('350x250')
# Label
    ttk.Label(window, text="Select the Month :",
              font=("Times New Roman", 10)).grid(column=0,
                                                 row=18, padx=10, pady=25)

    #n = tkinter.StringVar()
    # monthchoosen = ttk.Combobox(window, width=27,
   #                         textvariable=n)

    # Adding combobox drop down list
    monthchoosen['values'] = ('01',
                              '02',
                              '03',
                              '04',
                              '05',
                              '06',
                              '07',
                              '08',
                              '09',
                              '10',
                              '11',
                              '12')

    monthchoosen.grid(column=1, row=18)

# Shows february as a default value
    monthchoosen.current(1)

    ttk.Label(window, text="Select the Year :",
              font=("Times New Roman", 10)).grid(column=0,
                                                 row=21, padx=10, pady=25)

    #n = tkinter.StringVar()
   # yearchoosen = ttk.Combobox(window, width=27,
    #                        textvariable=n)

# Adding combobox drop down list
    yearchoosen['values'] = ('2019',
                             '2020',
                             '2021',
                             '2022',
                             '2023',
                             '2024',
                             '2025',
                             '2026',
                             '2027',
                             '2028',
                             '2029',
                             '2030')

    yearchoosen.grid(column=1, row=21)

# Shows february as a default value
    yearchoosen.current(1)

# Let the window wait for any events
    window.mainloop()


def check():
    print("check " + filename)
    print("check " + date)
    return(filename, date)
