import sqlite3

conn = sqlite3.Connection(
    r"C:\Users\2008d\Downloads\Telegram Desktop\Плавание МЧС 23.09.2019.cdb")

cursor = conn.cursor()
cursor.execute("SELECT * FROM sqlite_master where type='table';")
data = cursor.fetchall()
print(data)
