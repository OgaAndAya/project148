from tkinter import*
import random

root=Tk()
root.title("Picnic List")
root.geometry("400x400")

random_number_list= Label(root)
display_list_item= Label(root)
Listed_items: ['Bottle','Tiffin','ID Card','Chocolates','Chips','Tickets','Hanky']

def randomlist():
    randomlist= random.sample(range(0,7),1)
    random_number_list["text"]= "Random List:" + str(randomlist)
    randomlist.sort()
    display_list_item["text"]= "Sorted Random Numbers:" + str(randomlist)
    
btn=Button(root,text="Genereate Random List",command=randomlist)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

random_number_list.place(relx=0.5,rely=0.5,anchor=CENTER)
random_number_sorted_list.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()      


