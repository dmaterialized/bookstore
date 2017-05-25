from tkinter import *

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
list1=Listbox(window,height=7,width=140)
# list1.grid(row=1,column=0)
# need to add a span across more than one column (not just one grid square)
list1.grid(row=1,column=0,columnspan=4)
# attach a scrollbar
# tell the scrollbar about the list



# scrollbar setup
sb1=Scrollbar(window)
sb1.grid(row=1,column=5)
# attach the list to scrollbar, using configure and yscrollcommand.
list1.configure(yscrollcommand=sb1.set)
# let scrollbar know that the list is what is scrolling
sb1.configure(command=list1.yview)





# start everything
window.mainloop()
