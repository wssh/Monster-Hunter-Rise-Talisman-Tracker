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
    print('calling append')
    e.delete(0, END)
    e2.delete(0, END)
    update(lb3, skills)
    update(lb2, skills)
    
def checkkey1(event):
    print('calling checkkey1')
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
    print('calling checkkey2')
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
    print('calling update')
    # clear previous data
    lb.delete(0, 'end')
   
    # put new data
    for item in data:
        lb.insert('end', item)
  
