import gspread
import datetime
from tkinter import *
from oauth2client.service_account import ServiceAccountCredentials


# Get today's date
now = datetime.datetime.now()
date =str(now.strftime("%m/%d/%Y"))


# gspread code
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(creds)

sheet = client.open('WasteTracking').sheet1


def submitdata():
    row = [entry1.get(),entry2.get(),entry3.get()]
    index = 2
    sheet.insert_row(row,index)


# TKinter code
root = Tk()  # main window

label1 = Label(root,text="Date")
label2 = Label(root,text="Item")
label3 = Label(root,text="Source")

entry1 = Entry(root,bg="white",fg="blue")
entry1.insert(0,date)
entry2 = Entry(root,bg="white",fg="blue")
entry3 = Entry(root,bg="white",fg="blue")

button1=Button(root,text="Submit data",command=submitdata)

label1.grid(row=0)
entry1.grid(row=0,column=1)

label2.grid(row=2)
entry2.grid(row=2,column=1)

label3.grid(row=4)
entry3.grid(row=4,column=1)

button1.grid(row=6,column=1)

root.mainloop()  # display window on screen







