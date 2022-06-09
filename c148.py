from tkinter import *
import random

root = Tk()

root.title("LIST")
root.geometry("400x400")

random_number_list = Label(root)
random_number_sorted_list = Label(root)


def random_list():
    randomlist = random.sample(range(0,100),5)
    random_number_list["text"]="Random List : "+ str(randomlist)
    randomlist.sort()
    random_number_sorted_list["text"]="Sorted Random Numbers : "+ str(randomlist)
    
    
btn=Button(root,text="Generate Random Numbers",command=random_list)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)
    
random_number_list.place(relx=0.5,rely=0.5,anchor=CENTER)
random_number_sorted_list.place(relx=0.5,rely=0.6,anchor=CENTER)
root.mainloop()
