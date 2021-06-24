import tkinter as tk
from tkinter import *
from mhrlists import *
import gspread #

#sort the skill list from mhrlists, i could do these manually to save on operation time but kekw xd
skills.sort()
slots.sort()

#google sheets driver
gc = gspread.service_account(filename='credentials.json')
sh = gc.open("Charm Tracker")
worksheet_list = sh.worksheets()
worksheet = sh.get_worksheet(0)

#methods to drive ui behavior

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("Error")
    label = Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    b1 = Button(popup, text='Okay', command = popup.destroy)
    b1.pack()
    popup.mainloop()

def listboxEntry1Update(event):
    selection =  event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        e.delete(0, END)
        e.insert(0,data)

def listboxEntry2Update(event):
    selection =  event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        e2.delete(0, END)
        e2.insert(0,data)

def append():
    #print('calling append')
    skills1 = e.get()
    skills2 = e2.get()
    if skills1 == "" and skills2 != "":
        skills1 = skills2
        skills2 = ""
    #reset the entry + listboxes if the user appends garbage or duplicate skills
    if not (skills1 in skillset) or not (skills2 in skillset) or (skills1 ==  skills2):
        print("invalid talisman")
        e.delete(0, END)
        e2.delete(0, END)
        update(lb3, skills)
        update(lb2, skills)
        popupmsg("Invalid Talisman")
    level1 = skillLevel1_val.get()
    level2 = (skillLevel2_val.get(), "")[skills2==""]
    skills1 = skills1.replace(" ", "") + level1
    if skills2 != "":
        skills2 = skills2.replace(" ", "") +level2
    #print("Appending: Rarity: " + rarity_val.get() + ", Skill 1: " + skills1 + ", Skill 2: " + skills2 + ", Slots: " + slots_val.get())
    appendList = [rarity_val.get(), skills1, skills2, slots_val.get()]
    worksheet.append_row(appendList)
    worksheet.format("A2:A1000", {"horizontalAlignment": "RIGHT"})
    print(appendList)
    e.delete(0, END)
    e2.delete(0, END)
    update(lb3, skills)
    update(lb2, skills)
    
def checkkey1(event):
    #print('calling checkkey1')
    value = event.widget.get()
    print(value)
      
    # get data from skills
    if value == '':
        data = skills
    else:
        data = []
        for item in skills:
            if value.lower() in item.lower():
                data.append(item)                
   
    # update data in listbox
    update(lb2, data)

def checkkey2(event):
    #print('calling checkkey2')
    value = event.widget.get()
    print(value)
      
    # get data from skills
    if value == '':
        data = skills
    else:
        data = []
        for item in skills:
            if value.lower() in item.lower():
                data.append(item)                
   
    # update data in listbox
    update(lb3, data)
   
def update(lb, data):
    #print('calling update')
    # clear previous data
    lb.delete(0, 'end')
   
    # put new data
    for item in data:
        lb.insert('end', item)
  
# ui code how do you ever make this readable and clean?????? KEKW
root = Tk()
root.title("Talisman Tracker")

#labelframe0 for rarity+slots+append button
label_frame3 = LabelFrame(root)
label_frame3.pack(side = 'left')
label_frame0 = LabelFrame(label_frame3, text = 'Rarity and Slots')
label_frame0.pack()
label_frame5 = LabelFrame(label_frame3, text = 'Send it')
label_frame5.pack()
raritylabel = Label(label_frame0, text = 'Rarity')
slotslabel = Label(label_frame0, text = 'Slots')
rarity_val = StringVar(label_frame0)
rarity_val.set("7")
rarity_menu = OptionMenu(label_frame0, rarity_val, *rarity)
raritylabel.pack()
rarity_menu.pack()
slots_val = StringVar(label_frame0)
slots_val.set('0')
slots_menu = OptionMenu(label_frame0, slots_val, *slots)
slotslabel.pack()
slots_menu.pack()


#labelframe1 for 1st skill
label_frame1 = LabelFrame(root, text="Skill 1")
label_frame1.pack(side = 'left') 
#creating entry box
e = Entry(label_frame1)
e.pack() 
#creating list box
lb2 = Listbox(label_frame1, height = 11)
lb2.pack()
update(lb2, skills)
#skill level dropdown
skillLevel1 = Label(label_frame1, text = 'Skill 1 Level')
skillLevel1.pack()
skillLevel1_val = StringVar(label_frame1)
skillLevel1_menu = OptionMenu(label_frame1,  skillLevel1_val, *skilllevel)
skillLevel1_val.set('1')
skillLevel1_menu.pack()             


#labelframe2 for second skill
label_frame2 = LabelFrame(root, text="Skill 2")
label_frame2.pack(side = 'left')
#creating 2nd entry box
e2 = Entry(label_frame2)
e2.pack()
#creating 2nd list box
lb3 = Listbox(label_frame2, height = 11)
lb3.pack()
#2nd skill level drop down
skillLevel2 = Label(label_frame2, text = 'Skill 2 Level')
skillLevel2.pack()
skillLevel2_val = StringVar(label_frame2)
skillLevel2_menu = OptionMenu(label_frame2,  skillLevel2_val, *skilllevel)
skillLevel2_val.set('1')
skillLevel2_menu.pack()
update(lb3, skills)


e.bind('<KeyRelease>', checkkey1)
e2.bind('<KeyRelease>', checkkey2)
lb2.bind('<<ListboxSelect>>', listboxEntry1Update)
lb3.bind('<<ListboxSelect>>', listboxEntry2Update)


appendButton = Button(label_frame5, text='Append', command=append)
appendButton.pack()
   
root.mainloop()
