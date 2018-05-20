from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename

def openFile():
    fname = askopenfilename(filetypes=(("Template files", "*.tplate"),
                                       ("HTML files", "*.html;*.htm"),
                                       ("All files", "*.*")))



def Start():
    pass

def aboutMe():
    tkinter.messagebox._show("Information","Program is finding genes names and sequences from added file.")
    return
app = Tk()
app.title('Procaryota genes')
app.geometry("460x460")

menubar = Menu(app)
filemenu = Menu(menubar,tearoff=0)

filemenu.add_separator()

filemenu.add_command(label='Quit', command= app.quit)

helpmenu =  Menu(menubar, tearoff=0)
helpmenu.add_cascade(label="About program", command=aboutMe)
menubar.add_cascade(label="Help",menu=helpmenu)
app.config(menu=menubar)

aboutStud = Text(app)
bla="bsfbsfbsfb"
aboutStud.insert(END,"Please add your fasta file")
aboutStud.pack()


button1 = Button(app, text="Add file", width=20,height=10, command=openFile)
button1.pack(side="left",padx=15,pady=15)

button2 = Button(app, text="Start", width=20,height=10, command=Start)
button2.pack(side="right",padx=15,pady=15)
#photo = PhotoImage(file="C:/Users/dell/Desktop/Genetic-Engineering.jpg")
#label = Label(root, image=photo)
#label.pack()

app.mainloop()
