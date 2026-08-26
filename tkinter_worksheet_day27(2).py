from tkinter import *
def button_clicked():
    print("Doing something")
window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

my_label = Label(text="GUI")
my_label.config(text="New GUI program")
my_label.pack()

button = Button(text="Click",command=button_clicked)
button.pack()

input = Entry(width=10)
print(input.get())
input.pack()

window.mainloop()