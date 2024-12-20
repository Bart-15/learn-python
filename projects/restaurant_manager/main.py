from tkinter import * 

application = Tk()


# Windows size
application.geometry('1020x630+0+0')

# Prevnt for maximizing
application.resizable(False, False)

# Window title
application.title("May Restaurant - Invoicing System")

# Window background color
application.config(bg='burlywood')

# Top panel
top_panel = Frame(application, bd=1, relief=FLAT)
top_panel.pack(side=TOP)

# Title tag
title_tag = Label(top_panel, text='Invoicing System', fg='azure4', font =('Dosis', 58), bg='burlywood', width=27)
title_tag.grid(row=0, column=0)

application.mainloop()