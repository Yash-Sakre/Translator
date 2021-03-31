from tkinter import *
from tkinter import ttk 
from googletrans import Translator, LANGUAGES

root=Tk()
root.geometry('1080x400')
root.resizable(0,0)
root.config(bg='light cyan')

root.title("Language Translator")
Label(root,text="LANGUAGE TRANSLATOR",font="arial 20 bold",bg='lavender').pack()

Label(root,text="Project Translator ",font='arial 15 bold',bg='lavender',width='20').pack(side='bottom')

Label(root,text='Enter Text',font='arial 15 bold',bg='lavender').place(x=250,y=70)

Input_text=Text(root,font='arial 10',height=13,wrap=WORD,padx=5,pady=5,width=60)
Input_text.place(x=40,y=120)

Label(root,text='Output language',font='arial 15 bold',bg='lavender').place(x=680,y=70)
Output_text=Text(root,font='arial 10',height=13,wrap=WORD,padx=5,pady=5,width=60)
Output_text.place(x=600,y=120)


language=list(LANGUAGES.values())

srce=ttk.Combobox(root,values=language,width=22)
srce.place(x=40,y=75)
srce.set('choose input language')

des=ttk.Combobox(root,values=language,width=22)
des.place(x=880,y=80)
des.set('choose Output language')

def Translate():
    translator=Translator()
    translated=translator.translate(text=Input_text.get(1.0,END),src=srce.get(),dest=des.get())

    Output_text.delete(1.0,END)
    Output_text.insert(END, translated.text)


trans=Button(root,text="Translate",font='arial 15 bold',pady=5,command=Translate,bg='goldenrod',activebackground='sky blue')

trans.place(x=485,y=190)

root.mainloop()
