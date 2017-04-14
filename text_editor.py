from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile

filename = None

def newFile():
    global filename
    filename = 'Untitled'
    text.delete(0.0, END)

def openFile():
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename + '.txt', 'w')
    f.write(t)
    f.close()

def saveAs():
    global filename
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        print("Unable to save file...")

root = Tk()
root.title("Sevgin's Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = Text(root, width=400, height=400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As...", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label='Quit', command=root.quit)

menubar.add_cascade(label='File', menu=filemenu)

root.config(menu=menubar)
root.mainloop()