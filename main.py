from tkinter import *
from tkinter import messagebox 
import customtkinter
from PIL import ImageTk, Image
import re
import random

root = customtkinter.CTk()

root.title('Farbige Boxen')

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
root.iconbitmap('/Users/german/Documents/Coding/Python projects/My coding projects/GUI/Tkinter/Monopoly/favicon.ico')
root.geometry("1000x500")
root.configure(bg='black')

color='white'
colors = ['blue', 'red', 'green', 'yellow', 'orange', 'pink', 'purple']



def color_change():
    button_1.configure(bg=random.choice(colors), fg_color=random.choice(colors))
    button_2.configure(bg=random.choice(colors), fg_color=random.choice(colors))
    button_3.configure(bg=random.choice(colors), fg_color=random.choice(colors))
    button_4.configure(bg=random.choice(colors), fg_color=random.choice(colors))
    button_5.configure(bg=random.choice(colors), fg_color=random.choice(colors))
    button_6.configure(bg=random.choice(colors), fg_color=random.choice(colors))
      
        


game_frame = customtkinter.CTkFrame(master=root,
                               width=1000,
                               height=500,
                               corner_radius=10,
                               bg='black',
                               fg_color='black',)


button_1 = customtkinter.CTkButton(root, command=color_change, width=100,
                                height=40,
                                corner_radius=8,
                                text="",
                                fg_color=color,
                                text_font=('Times New Roman', 26),
                            bg_color='black',
                            hover_color=None
                                )
button_2 = customtkinter.CTkButton(root, command=color_change, width=100,
                                height=40,
                                corner_radius=8,
                                text="",
                                fg_color=color,
                                text_font=('Times New Roman', 26),
                            bg_color='black',
                            hover_color=None
                                )
button_3 = customtkinter.CTkButton(root, command=color_change, width=100,
                                height=40,
                                corner_radius=8,
                                text="",
                                fg_color=color,
                                text_font=('Times New Roman', 26),
                            bg_color='black',
                            hover_color=None
                                )
button_4 = customtkinter.CTkButton(root, command=color_change, width=100,
                                height=40,
                                corner_radius=8,
                                text="",
                                fg_color=color,
                                text_font=('Times New Roman', 26),
                            bg_color='black',
                            hover_color=None
                                )
button_5 = customtkinter.CTkButton(root, command=color_change, width=100,
                                height=40,
                                corner_radius=8,
                                text="",
                                fg_color=color,
                                text_font=('Times New Roman', 26),
                            bg_color='black',
                            hover_color=None
                                )
button_6 = customtkinter.CTkButton(root, command=color_change, width=100,
                                height=40,
                                corner_radius=8,
                                text="",
                                fg_color=color,
                                text_font=('Times New Roman', 26),
                            bg_color='black',
                            hover_color=None
                                )
button_7 = customtkinter.CTkButton(root, command=color_change, width=100,
                                height=40,
                                corner_radius=8,
                                text="",
                                fg_color=color,
                                text_font=('Times New Roman', 26),
                            bg_color='black',
                            hover_color=None
                                )
                                









#Packing them on the screen

game_frame.grid(row=0, column=0, columnspan=4, rowspan=6, sticky='news')

button_1.grid(row=0, column=0, sticky='nwes')
button_2.grid(row=0, column=1, sticky='nwes')
button_3.grid(row=0, column=2, sticky='nwes')
button_4.grid(row=0, column=3, sticky='nwes')
button_5.grid(row=1, column=0, sticky='nwes')
button_6.grid(row=1, column=1, sticky='nwes')
button_7.grid(row=1, column=2, sticky='nwes')




root.mainloop()