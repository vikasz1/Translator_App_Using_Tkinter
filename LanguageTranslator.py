from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
translator = Translator(service_urls=['translate.googleapis.com'])

root = Tk()
root.geometry('1080x400')
root.resizable(0, 0)
root.title("Virtual Language Translator")
root.config(bg='light blue')
root.wm_iconbitmap('lang.ico')

# heading
Label(root, text="LANGUAGE TRANSLATOR", font="arial 20 bold", bg='cyan').pack(side='top')
Label(root, text="MINI PROJECT", font='arial 20 bold', bg='cyan', width='20').pack(side='bottom')

# INPUT AND OUTPUT TEXT WIDGET
Label(root, text="Input", font='arial 13 bold', bg='white smoke').place(x=200, y=60)
Input_text = Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
Input_text.place(x=30, y=100)

Label(root, text="Output", font='arial 13 bold', bg='white smoke').place(x=780, y=60)
Output_text = Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
Output_text.place(x=600, y=100)

##################
#language selection dropdown menu
language = list(LANGUAGES.values())
src_lang = ttk.Combobox(root, values=language, width=22,state = 'readonly')
src_lang.current(language.index("english"))
src_lang.place(x=20, y=60)
# src_lang.set('Input Language')

dest_lang = ttk.Combobox(root, values=language, width=22,state='readonly')
dest_lang.place(x=890, y=60)
dest_lang.current(language.index("hindi"))
# dest_lang.set('Output Language')


########################################  Define function #######

def Translate_function():
    translated = translator.translate(text=Input_text.get(1.0, END), src=src_lang.get(), dest=dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)


##########  Translate Button ########
trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=Translate_function, bg='royal blue',
                   activebackground='sky blue')
trans_btn.place(x=490, y=180)

root.mainloop()

