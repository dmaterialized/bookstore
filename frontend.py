# /// ------------
# \\\ BOOKSTORE
# ///  creates a bookstore db with interface.
# \\\   | version: 0.1.4
# ///   | date: 2017.06.04 / initial: 2017.05.24
# \\\   |
# ///   |
# \\\   | TODO:
# ///   | - scripting for each button
# \\\   | - fix delete button error
# ///   | - ensure that search works on any capitalization
# \\\   |
# ///   |
# \\\   |
# /\/\     -------------------------------------

from tkinter import *
import backend
print("Frontend initialized.")


# ============================================
# ======= F U N C T I O N S ##################
# ============================================

def get_selected_row(event):
    # index=list1.curselection()
    # print("the current selection is: ")
    # print(index)

    # needs to change to a selected Tuple, so needs to be converted
    #           from a (14,) to a 14.

#  doing over
    # index=list1.curselection()[0] # indicates a tuple
    # print(index)
    # it worked!


#   doing over again in order to print actual content of the row item
    # in order to span outside functions, this needs to be a GLOBAL
    # FIRST GLOBAL !!
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)

    # this trick takes the full content of each indexed row
    #           and stores in selected_tuple
    #
    # from debugging:
    # print(selected_tuple)
    # return(selected_tuple)
    #           no longer needed as tuple is now a global
#
# AUTOFILL FEATURE
# next we want to fill entry fields with values of selected tuple
# let's create autofill!

    # in each field e1-e4, first clear out all Entry...
    e1.delete(0,END) # clear
    e1.insert(END,selected_tuple[1]) # show title
    e2.delete(0,END) # clear
    e2.insert(END,selected_tuple[2]) # show author
    e3.delete(0,END) # clear
    e3.insert(END,selected_tuple[3]) # show year
    e4.delete(0,END) # clear
    e4.insert(END,selected_tuple[4]) # show isbn

    print("currently selected:"+str(selected_tuple))
    # unused
    # index=list1.curselection()
    # selected_tuple=list1.get(index)
    # return (index)
    # print(selected_tuple)

def view_command():
    list1.delete(0,END)
        #clear existing data here so that Show All
            # won't duplicate its output each time.
    # iterate through a tuple
    for row in backend.view():
        list1.insert(END,row)
    print("Showing all records.")


def search_command(): # use the existing StringVar for search input
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(), year_text.get(),isbn_text.get()):
            # the get is because
            # in this situation
            # each of the text fields
            # is a variable and we
            # need to string it.
        list1.insert(END,row)
    print("Ran a search.")

def add_command():
    backend.insert(title_text.get(),author_text.get(), year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(), year_text.get(),isbn_text.get()))
    print("Item added.")


def delete_command():
    # grab id of the selected row and send it to backend script
    #tkinter bind command is used to connect a widget to a command
    # backend.delete(id) - works
    # backend.delete(get_selected_row()[0])
    # doesn't work until you call func with the arg 'event'
    backend.delete(selected_tuple[0])
    print("Item deleted")
    # then refresh the list
    view_command()

def update_command():
    # unlike the delete command, this one requires
    #           full tuple with each
    #           value separated
    backend.update(selected_tuple[0],selected_tuple[1],selected_tuple[2],selected_tuple[3],selected_tuple[4])
    print("Updated.")


# //////////////////////////////////////
# ==== E N D   F U N C T I O N S ======
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\




window=Tk()

# ====== l a b e l   s e t u p ===============
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

# ====== e n t r y   f i e l d   s e t u p =====
e1=Entry(window,textvariable=title_text)
# textvariable means that the content of the Entry can be called later
e1.grid(row=0,column=1)

e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

e3=Entry(window,textvariable=year_text)
e3.grid(row=0,column=5)

e4=Entry(window,textvariable=isbn_text)
e4.grid(row=0,column=7)


# == l i s t b o x   s e t u p =========
list1=Listbox(window,height=40,width=60)
# list1.grid(row=1,column=0) doesn't do enough.
# need to add a span across more than one column (not just one grid square)
list1.grid(row=2,column=0,columnspan=4)

# == B I N D I N G S =============
# create bind so that a list selection can be parsed.
list1.bind('<<ListboxSelect>>',get_selected_row)
# ========================================

# == s c r o l l b a r   s e t u p ==========
# attach a scrollbar
# tell the scrollbar about the list
sb1=Scrollbar(window)
sb1.grid(row=2,column=4)
# attach the list to scrollbar, using configure and yscrollcommand.
list1.configure(yscrollcommand=sb1.set)
# let scrollbar know that the list is what is scrolling
sb1.configure(command=list1.yview)


# b u t t o n   s e t u p =========

# show all / close / add / delete / update / search
b1=Button(window,text="Show All",command=view_command)
b1.grid(row=2,column=4)

b2=Button(window,text="Close")
b2.grid(row=4,column=7)

b3=Button(window,text="Add Entry",command=add_command)
b3.grid(row=4,column=4)

b4=Button(window,text="DELETE",command=delete_command)
b4.grid(row=4,column=1)

b5=Button(window,text="Update Entry",command=update_command)
b5.grid(row=4,column=3)

b6=Button(window,text="Search",command=search_command)
b6.grid(row=2,column=7)







# start everything =======
window.mainloop()
