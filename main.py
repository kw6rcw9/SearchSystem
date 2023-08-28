import tkinter.messagebox
from tkinter import *
import webbrowser
import urllib.parse

root = Tk()
root['bg'] = '#fafafa'
root.title('Search System')
root.geometry('300x110')

def search(event = None):
    if len(text_field.get()) > 2:
        webbrowser.open("https://www.google.com/search?q=" + urllib.parse.quote(text_field.get()))


frame = Frame(root, bg='#fafafa')
frame.place(relwidth=0.8, relx=0.1, relheight=0.9, rely=0.05)

Label(frame, text='Search', bg='#fafafa', fg='#000').pack()

text_field = Entry(frame, width=50, bg='#fafafa', fg='#000')
text_field.bind('<Return>', search)
text_field.pack()

btn = Button(frame, text='Find', width=10, highlightbackground='#fafafa', activeforeground='#E06249', command = search)
btn.pack()


root.wm_attributes('-topmost', True)
root.mainloop()

