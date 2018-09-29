import gspread
from tkinter import *
from oauth2client.service_account import ServiceAccountCredentials

# gspread code
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(creds)

sheet = client.open('WasteTracking').sheet1
##

# tkinter code
root = Tk()  # main window

label1 = Label(root,text="Date")
label2 = Label(root,text="Item")
label3 = Label(root,text="Source")

entry1 = Entry(root,bg="white",fg="blue")
entry2 = Entry(root,bg="white",fg="blue")
entry3 = Entry(root,bg="white",fg="blue")

button1=Button(root,text="Submit data",command=submitdata())

label1.grid(row=0)
entry1.grid(row=0,column=1)

label2.grid(row=2)
entry2.grid(row=2,column=1)

label3.grid(row=4)
entry3.grid(row=4,column=1)

button1.grid(row=6,column=1)

date = entry1.get()
item = entry2.get()
source = entry3.get()

print(date)
print(item)
print(source)
root.mainloop()  # display window on screen
##

def submitdata():
    print("boise")



submitdata()
#row = [date,item,source]

#index = 2

#sheet.insert_row(row,index)
