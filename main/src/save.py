import sqlite3
import os

FILE_PATH = "main/data/"

def save_data(datas):

    os.makedirs(FILE_PATH, exist_ok=True)

    conn = sqlite3.connect(FILE_PATH + "data.db")
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS qr_data
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       url TEXT,
                       box_size INTEGER,
                       border_size INTEGER,
                       name TEXT,
                       background_color TEXT,
                       fill_color TEXT)''')
    
    cursor.execute('''INSERT INTO qr_data (url, box_size, border_size, name, background_color, fill_color)
                      VALUES (?, ?, ?, ?, ?, ?)''',
                   (datas["url"], datas["box_size"], datas["border_size"], datas["name"], datas["background_color"], datas["fill_color"]))
    
    conn.commit()
    conn.close()

def load_all():
    conn = sqlite3.connect(FILE_PATH + "data.db")
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM qr_data''')
    
    rows = cursor.fetchall()
    
    conn.close()
    
    return rows