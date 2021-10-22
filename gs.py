import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import sqlite3
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "C:/example/cred.json")
client = gspread.authorize(creds)
sheet = client.open("Attendance").sheet1
data = sheet.get_all_records()
print(data)
pprint(data)
#conn = sqlite3.connect('c:/example/Students.db')
#c = conn.cursor()
#val = c.execute(" SELECT * from code")
#cont = val.fetchall


def sheets():
    conn = sqlite3.connect('c:/example/Students.db')
    c = conn.cursor()
    val = c.execute(" SELECT * from code")
    cont = val.fetchall
    row = 2
    c.execute("PRAGMA table_info(code)")
    head = c.fetchall()
    header = []

    for i in head:
        header.append(i[1])
        print(header)
    sheet.resize(rows=1)
    sheet.resize(rows=100)
    sheet.delete_row(1)
    # for i in range(1, 500):
    #   sheet.delete_row(i)
    # time.sleep(0.10)
    sheet.insert_row(header, 1)
    for tuple in c.execute('SELECT * FROM code'):
        sheet.insert_row(tuple, row)
        row = row+1
        print("\n")
        print(tuple)
        time.sleep(1.5)
