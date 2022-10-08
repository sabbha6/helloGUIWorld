# Hello GUI World
import tkinter
from tkinter import BOTH, StringVar, END
from PIL import ImageTk, Image

# Define window
root = tkinter.Tk()
root.title("Hello GUI World")
root.iconbitmap('wave.png')
root.geometry('600x400')

# Coloring
root_color = '#F7FFF6'
input_color = '#BCEBCB'
output_color = '#87D68D'
text_color = '#55505C'


# Define function
def submit_name():
    """Say Hello to USER"""
    # Create label
    if case_style.get() == 'normal':
        name_label = tkinter.Label(output_frame,
                                   text="Hello " + name.get() + "! Welcome & keep learning Tkinter!!😁",
                                   bg=output_color, fg=text_color)
    elif case_style.get() == 'upper':
        name_label = tkinter.Label(output_frame, text=(
                    "Hello " + name.get() + "! Welcome & keep learning Tkinter!!😁").upper(),
                                   bg=output_color, fg=text_color)
    elif case_style.get() == 'lower':
        name_label = tkinter.Label(output_frame, text=(
                    "Hello " + name.get() + "! Welcome & keep learning Tkinter!!😁").lower(),
                                   bg=output_color, fg=text_color)

    # bring it on the screen
    name_label.pack(side='top', anchor='n', padx=5, pady=5)

    # clear the input
    name.delete(0, END)


# Define layout
# define frames
input_frame = tkinter.LabelFrame(root, bg=input_color)
output_frame = tkinter.LabelFrame(root, bg=output_color)
input_frame.pack(pady=20)
output_frame.pack(padx=10, pady=(0, 10), fill=BOTH, expand=True)

# create widgets
name = tkinter.Entry(input_frame, text='Enter your name', width=20)
submit_btn = tkinter.Button(input_frame, text='Submit',
                            highlightbackground=input_color,
                            command=submit_name)
name.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
submit_btn.grid(row=0, column=2, padx=10, pady=10, ipadx=0, ipady=0)

# create radio button
case_style = StringVar()
case_style.set('normal')
normal_radio = tkinter.Radiobutton(input_frame, text='Normal Case',
                                   variable=case_style, value='normal',
                                   bg=input_color, fg=text_color)
upper_radio = tkinter.Radiobutton(input_frame, text='Upper Case',
                                  variable=case_style, value='upper',
                                  bg=input_color, fg=text_color)
lower_radio = tkinter.Radiobutton(input_frame, text='Lower Case',
                                  variable=case_style, value='lower',
                                  bg=input_color, fg=text_color)
normal_radio.grid(row=1, column=0, padx=5, pady=5, ipadx=0, ipady=0)
upper_radio.grid(row=1, column=1, padx=5, pady=5, ipadx=0, ipady=0)
lower_radio.grid(row=1, column=2, padx=5, pady=5, ipadx=0, ipady=0)

# Add Image
wlcm_img = ImageTk.PhotoImage(Image.open('welcm.png'), height=20)
wlcm_label = tkinter.Label(output_frame, image=wlcm_img, width=100, height=200,
                           bg=output_color)
wlcm_label.pack(side='left', anchor='w', padx=5, pady=5)

root.config(bg=root_color)

# Running root window
root.mainloop()
