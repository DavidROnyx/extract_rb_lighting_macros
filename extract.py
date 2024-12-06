import sqlite3
import os

fixture={}

conn = sqlite3.connect(os.getenv("HOME") + '/Library/Application Support/Pioneer/rekordbox6/LightingDB/macro.db3')

cursor1 = conn.cursor()
cursor2 = conn.cursor()

# récupère les noms de fixture
cursor1.execute("SELECT id,name FROM macro_fixture")
row = cursor1.fetchone()
while row is not None:
    fixture[row[0]]=row[1]
    row = cursor1.fetchone()

# récupère la liste des macros
cursor1.execute("SELECT id,name FROM macro")

# extrait les data de chaque macros
dirname='data'
if not os.path.exists(dirname):
    os.makedirs(dirname)
os.chdir(dirname)    
row = cursor1.fetchone()
while row is not None:
    dirname=str(row[0]) + "-" + str(row[1])
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    cursor2.execute("SELECT macro_fixture_id,data FROM macro_data WHERE macro_id="+ str(row[0]))
    data=cursor2.fetchone()
    while data is not None:
        filename=dirname+"/"+str(data[0])+"-"+str(fixture[data[0]])
        file=open(filename,"w")
        file.write(str(data[1]))
        file.close()
        data=cursor2.fetchone()
    row= cursor1.fetchone()
conn.close()





