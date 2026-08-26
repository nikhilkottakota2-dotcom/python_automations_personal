from tkinter import *

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

# Create a label once
my_label = Label(text="Hello!", font=("Times New Roman", 24, "bold"))
my_label.pack()

def clicked():
    new_text = input.get()
    my_label.config(text=new_text)  # update existing label

button = Button(text="Click Here", command=clicked)
button.pack()

input = Entry()
input.pack()

window.mainloop()





















# def add(*args):

#     sum = 0
#     for n in args:
#         sum += n

#     return sum

# print(add(3,2,5,6,7))

# def greet(name,dept):
#     print(f"Hi {name}")
#     print(f"Are You From {dept} Department")

# # greet(dept="CS",name="Nikhil")
# greet(dept="CS","Nikhil")

# def greet(name,subject,dept="CS"):
#     print(f"Hi {name}")
#     print(f"Is your subject mastering is {subject}")
#     print(f"Are you from {dept} department")
# greet(name="Kottakota Nikhil",subject="Python")

# def name(*args):
#     print(args[0])
#     c=0
#     for i in args:
#         c = c+i

#     return c
# print(name(1,4,10,8,5))
# def info_person(*numbers,name):
#     print(numbers[0])
#     print(name)
# print(info_person(1,2,3,name="Kottakota Nikhil"))

# def info(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)
#     print("______________________________________")
# info(name="Kottakota Nikhil",Department="Computer Engineering",stipend="15000")
# info(name="Nikhil Kottakota",Department="Computer Engineering")