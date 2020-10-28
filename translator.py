from tkinter import *
from translate import Translator

window = Tk()
window.title("language translator")

# Add a grid
mainframe = Frame(window)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)


lan1 = StringVar(window)
lan2= StringVar(window)


def trans():
    translator = Translator(from_lan = lan1.get(), to_lang=lan2.get())
    translation = translator.translate(var.get())
    var1.set(translation)


#translator= Translator(to_lang="German")
#translation = translator.translate("Good Morning!")

choice = { " ENGLISH","TELUGU"}
lan1menu = OptionMenu( mainframe , lan1 , *choice)
Label(mainframe, text="select language").grid(row = 0 , column =1)
lan1menu.grid(row = 1, column=1)


lan2menu = OptionMenu( mainframe , lan2, *choice)
Label(mainframe, text="select language").grid(row = 0 , column =1)
lan2menu.grid(row = 1, column=2)


Label(mainframe, text ="enter text ").grid(row=2,column=0)
var = StringVar()
textbox = Entry(mainframe , textvariable = var).grid(row=2,column=1)




Label(mainframe, text ="output").grid(row=2,column=2)
var1 = StringVar()
textbox = Entry(mainframe , textvariable = var1).grid(row=2,column=3)

button = Button(mainframe,text= 'translate', command= trans).grid(row=3,column=1, columnspan=3)





window.mainloop()
