
from tkinter import *
import webbrowser
import urllib.parse

root = Tk()
root['bg'] = '#fafafa'
root.title('Search System')
root.geometry('300x150')
searchEngine = StringVar()
searchEngine.set('google')

def search(event = None):
    if len(text_field.get()) <= 2:
        return
    if searchEngine.get() == 'google':
        webbrowser.open("https://www.google.com/search?q=" + urllib.parse.quote(text_field.get()))
    elif searchEngine.get() == 'yandex':
        webbrowser.open("https://yandex.ru/search/?text=" + urllib.parse.quote(text_field.get()))

frame = Frame(root, bg='#fafafa')
frame.place(relwidth=0.8, relx=0.1, relheight=0.9, rely=0.05)

Label(frame, text='Search', bg='#fafafa', fg='#000', font=("Verdana", 20)).pack()

text_field = Entry(frame, width=50, bg='#fafafa', fg='#000')
text_field.bind('<Return>', search)
text_field.pack()

btn = Button(frame, text='Find', width=10, highlightbackground='#fafafa', activeforeground='#E06249', command=search)

btn.pack()

Radiobutton(frame, text='Google', value='google', variable=searchEngine).pack()
Radiobutton(frame, text='Yandex', value='yandex', variable=searchEngine).pack()

root.wm_attributes('-topmost', True)
root.mainloop()

