from tkinter import *
import backend
import time
    
def search_command():
    list1.delete(0,END)
    for row in backend.mydict(word_text.get()):
        list1.insert(END,'-'+row)
    k = list1.get(0,END)
    if len(k) == 0:
        list1.insert(END,"-----------------------------------------")
        list1.insert(END,"----SORRY, WORD NOT FOUND!!!----")
        list1.insert(END,"(Check your spelling or try another word)")
        #you can put in the get close matches function here
        list1.insert(END,"-----------------------------------------")
    else:
        ent1.delete(0,END)
        ent1.insert(END,backend.status(word_text.get()))
        list2.delete(0,END)
        list3.delete(0,END)
        for row in backend.bonus():
            from backend import bonus_word
            list3.insert(END,bonus_word)
            list2.insert(END,'-'+row)

def update_command():
    backend.update(word_text.get())
    lbl3.configure(text="DONE")
    lbl3.update()
    time.sleep(3)
    lbl3.configure(text="")
    ent1.delete(0,END)
    ent1.insert(END,'imp')

window = Tk()
window.title("AB's Dictionary")
window.geometry('550x280')

lbl = Label(window, text = "Enter Word")
lbl.grid(column=0,row=0)

lbl2 = Label(window, text = "Status")
lbl2.grid(column=0,row=1)

lbl3 = Label(window, text = "")
lbl3.grid(column=3,row=1)

word_text = StringVar()
ent = Entry(window,textvariable = word_text)
ent.grid(column=1,row=0)

btn = Button(window, text = "Search",command=search_command)
btn.grid(column=2, row=0)
window.bind('<Return>', lambda event=None: btn.invoke())

status_text = StringVar()
ent1 = Entry(window,textvariable = status_text)
ent1.grid(column=1,row=1)

btn1 = Button(window, text = "Mark 'imp'",command=update_command)
btn1.grid(column=2, row=1)

list1 = Listbox(window, height=6,width=85)
list1.grid(row=2,column=0,rowspan=6,columnspan=4)

sb1 = Scrollbar(window, orient='horizontal')
list1.configure(xscrollcommand=sb1.set)
sb1.configure(command=list1.xview)
sb1.grid(row=8,column=0,columnspan=4)

list3 = Listbox(window,height=1)
list3.grid(row=8,column=0)

#list1.bind('<<ListboxSelect>>',get_selected_row)
'''
btn = Button(window, text = "Search",command=search_command)
btn.grid(column=2, row=0)
'''
list2 = Listbox(window, height=5,width=85)
list2.grid(row=11,column=0,columnspan=4)

window.mainloop()
