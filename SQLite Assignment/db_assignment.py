#
#   Python Version: Python 3.8.5
#
#   Author: Casey Levy
#
#
#   Purpose: SQLite and Python assignment creatng a database
#           and modifying data
#
#
#
#

import sqlite3


conn = sqlite3.connect('DB_Assignment.db')

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')



# connecting to DB and creating table with column
with conn:
    db = conn.cursor()
    db.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_files TEXT \
        )")


# Specifying which file extension to add to DB, in this case it is .txt
    for myFiles in fileList:
        if myFiles.endswith(".txt"):
            print(myFiles)
            db.execute("INSERT INTO tbl_files(col_files) VALUES (?)", (myFiles,))
            

# Printing the selected files 
    with conn:
        db = conn.cursor()
        db.execute("SELECT col_files FROM tbl_files")
        printAll = db.fetchall()
        print(printAll)
    conn.commit()
conn.close()







