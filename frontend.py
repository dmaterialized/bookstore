# /// ------------
# \\\ BOOKSTORE
# ///  creates a bookstore db with interface.
# \\\   | version: 0.1.2
# ///   | date: 2017.05.24
# \\\   |
# ///   | TODO:
# \\\   | - all backend db
# ///   | - scripting for each button
# \\\   | - finalize layout
# ///   |
# \\\   |
#      -------------------------------------



from tkinter import *
import backend

window=Tk()

# l a b e l   s e t u p
l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=0,column=4)

l4=Label(window,text="ISBN")
l4.grid(row=0,column=6)

#set up stringvar to store field values
title_text=StringVar()
author_text=StringVar()
isbn_text=StringVar()
year_text=StringVar()

# e n t r y   f i e l d   s e t u p
e1=Entry(window,textvariable=title_text)
# textvariable means that the content of the Entry can be called later
e1.grid(row=0,column=1)

e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

e3=Entry(window,textvariable=year_text)
e3.grid(row=0,column=5)

e4=Entry(window,textvariable=isbn_text)
e4.grid(row=0,column=7)



# l i s t b o x   s e t u p
list1=Listbox(window,height=40,width=60)
# list1.grid(row=1,column=0) doesn't do enough.
# need to add a span across more than one column (not just one grid square)
list1.grid(row=2,column=0,columnspan=4)


# attach a scrollbar
# tell the scrollbar about the list
# scrollbar setup
sb1=Scrollbar(window)
sb1.grid(row=2,column=4)
# attach the list to scrollbar, using configure and yscrollcommand.
list1.configure(yscrollcommand=sb1.set)
# let scrollbar know that the list is what is scrolling
sb1.configure(command=list1.yview)


# b u t t o n   s e t u p

# move update over to middle, add to next one, close window to ending

# update / add / close
b1=Button(window,text="Show All")
b1.grid(row=2,column=4)

b2=Button(window,text="Close")
b2.grid(row=4,column=7)

b3=Button(window,text="Add Entry")
b3.grid(row=4,column=4)

b4=Button(window,text="DELETE")
b4.grid(row=4,column=1)

b5=Button(window,text="Update Entry")
b5.grid(row=4,column=3)

b6=Button(window,text="Search")
b6.grid(row=2,column=7)





# start everything
window.mainloop()