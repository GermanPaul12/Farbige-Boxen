from tkinter import *
from tkinter import messagebox 
import customtkinter
import random

root = customtkinter.CTk()

root.title('Farbige Boxen')

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
root.iconbitmap('/Users/german/Documents/Coding/Python projects/My coding projects/GUI/Tkinter/Monopoly/favicon.ico')
root.geometry("1000x450")
root.configure(bg='black')

color='white'
colors = ['blue', 'red']



def color_change():
    global button_colors
    button_1.configure(bg=random.choice(colors), fg_color=random.choice(colors))
    button_2.configure(bg=random.choice(colors), fg_color=random.choice(colors))
    button_3.configure(bg=random.choice(colors), fg_color=random.choice(colors))
    button_4.configure(bg=random.choice(colors), fg_color=random.choice(colors))
    button_5.configure(bg=random.choice(colors), fg_color=random.choice(colors))
    button_6.configure(bg=random.choice(colors), fg_color=random.choice(colors))
    button_7.configure(bg=random.choice(colors), fg_color=random.choice(colors))
    button_8.configure(bg=random.choice(colors), fg_color=random.choice(colors))
    button_9.configure(bg=random.choice(colors), fg_color=random.choice(colors))
    button_10.configure(bg=random.choice(colors), fg_color=random.choice(colors))
    button_11.configure(bg=random.choice(colors), fg_color=random.choice(colors))
    button_12.configure(bg=random.choice(colors), fg_color=random.choice(colors))
    button_13.configure(bg=random.choice(colors), fg_color=random.choice(colors))
    button_14.configure(bg=random.choice(colors), fg_color=random.choice(colors))
    button_15.configure(bg=random.choice(colors), fg_color=random.choice(colors))
    button_16.configure(bg=random.choice(colors), fg_color=random.choice(colors))
    button_17.configure(bg=random.choice(colors), fg_color=random.choice(colors))
    button_18.configure(bg=random.choice(colors), fg_color=random.choice(colors))
    button_19.configure(bg=random.choice(colors), fg_color=random.choice(colors))
    button_20.configure(bg=random.choice(colors), fg_color=random.choice(colors))      
    button_colors = set([button_1.fg_color, button_2.fg_color, button_3.fg_color, 
                     button_4.fg_color, button_5.fg_color, button_6.fg_color, 
                     button_7.fg_color, button_8.fg_color, button_9.fg_color, 
                     button_10.fg_color, button_11.fg_color, button_12.fg_color, 
                     button_13.fg_color, button_14.fg_color, button_15.fg_color, 
                     button_16.fg_color, button_17.fg_color, button_18.fg_color, 
                     button_19.fg_color, button_20.fg_color])  

    if len(button_colors) == 1:
        messagebox.showinfo(title='Important Message', message='You won!')       

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
button_8 = customtkinter.CTkButton(root, command=color_change, width=100,
                            height=40,
                            corner_radius=8,
                            text="",
                            fg_color=color,
                            text_font=('Times New Roman', 26),
                        bg_color='black',
                        hover_color=None
                            )


button_9 = customtkinter.CTkButton(root, command=color_change, width=100,
                            height=40,
                            corner_radius=8,
                            text="",
                            fg_color=color,
                            text_font=('Times New Roman', 26),
                        bg_color='black',
                        hover_color=None
                            )


button_10 = customtkinter.CTkButton(root, command=color_change, width=100,
                            height=40,
                            corner_radius=8,
                            text="",
                            fg_color=color,
                            text_font=('Times New Roman', 26),
                        bg_color='black',
                        hover_color=None
                            )


button_11 = customtkinter.CTkButton(root, command=color_change, width=100,
                            height=40,
                            corner_radius=8,
                            text="",
                            fg_color=color,
                            text_font=('Times New Roman', 26),
                        bg_color='black',
                        hover_color=None
                            )


button_12 = customtkinter.CTkButton(root, command=color_change, width=100,
                            height=40,
                            corner_radius=8,
                            text="",
                            fg_color=color,
                            text_font=('Times New Roman', 26),
                        bg_color='black',
                        hover_color=None
                            )


button_13 = customtkinter.CTkButton(root, command=color_change, width=100,
                            height=40,
                            corner_radius=8,
                            text="",
                            fg_color=color,
                            text_font=('Times New Roman', 26),
                        bg_color='black',
                        hover_color=None
                            )


button_14 = customtkinter.CTkButton(root, command=color_change, width=100,
                            height=40,
                            corner_radius=8,
                            text="",
                            fg_color=color,
                            text_font=('Times New Roman', 26),
                        bg_color='black',
                        hover_color=None
                            )


button_15 = customtkinter.CTkButton(root, command=color_change, width=100,
                            height=40,
                            corner_radius=8,
                            text="",
                            fg_color=color,
                            text_font=('Times New Roman', 26),
                        bg_color='black',
                        hover_color=None
                            )


button_16 = customtkinter.CTkButton(root, command=color_change, width=100,
                            height=40,
                            corner_radius=8,
                            text="",
                            fg_color=color,
                            text_font=('Times New Roman', 26),
                        bg_color='black',
                        hover_color=None
                            )                 
button_17 = customtkinter.CTkButton(root, command=color_change, width=100,
                        height=40,
                        corner_radius=8,
                        text="",
                        fg_color=color,
                        text_font=('Times New Roman', 26),
                    bg_color='black',
                    hover_color=None
                        )

button_18 = customtkinter.CTkButton(root, command=color_change, width=100,
                        height=40,
                        corner_radius=8,
                        text="",
                        fg_color=color,
                        text_font=('Times New Roman', 26),
                    bg_color='black',
                    hover_color=None
                        )

button_19 = customtkinter.CTkButton(root, command=color_change, width=100,
                        height=40,
                        corner_radius=8,
                        text="",
                        fg_color=color,
                        text_font=('Times New Roman', 26),
                    bg_color='black',
                    hover_color=None
                        )

button_20 = customtkinter.CTkButton(root, command=color_change, width=100,
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
button_8.grid(row=1, column=3, sticky='nwes')
button_9.grid(row=2, column=0, sticky='nwes')
button_10.grid(row=2, column=1, sticky='nwes')
button_11.grid(row=2, column=2, sticky='nwes')
button_12.grid(row=2, column=3, sticky='nwes')
button_13.grid(row=3, column=0, sticky='nwes')
button_14.grid(row=3, column=1, sticky='nwes')
button_15.grid(row=3, column=2, sticky='nwes')
button_16.grid(row=3, column=3, sticky='nwes')
button_17.grid(row=4, column=0, sticky="nwes")
button_18.grid(row=4, column=1, sticky="nwes")
button_19.grid(row=4, column=2, sticky="nwes")
button_20.grid(row=4, column=3, sticky="nwes")

'''
for i in range(100000):
    color_change()
    if len(button_colors) == 1:
        print(i)
        messagebox.showinfo(title='Important Message', message='You won!')
        break
'''

root.mainloop()
