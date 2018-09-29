import gspread
from tkinter import *
from oauth2client.service_account import ServiceAccountCredentials

# gspread code
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(creds)

sheet = client.open('WasteTracking').sheet1

date = input()
##

# tkinter code
root = Tk()  # main window

root.mainloop()  # display window on screen
##



#row = ["this","is","awesome!"]

#index = 2

#sheet.insert_row(row,index)
