# # import tkinter
# # window = tkinter.Tk()
# # window.title("My First GUI program")
# # window.minsize(width=500,height=300)
# # my_label = tkinter.Label(text="I Am Brilliant",font=("Times New Roman",24,"bold"))
# # my_label.pack()#package functions
# # window.mainloop()

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

def greet(name,subject,dept="CS"):
    print(f"Hi {name}")
    print(f"Is your subject mastering is {subject}")
    print(f"Are you from {dept} department")
greet(name="Kottakota Nikhil",subject="Python")