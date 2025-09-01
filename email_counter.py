import sqlite3

db =sqlite3.connect('emaildb.sqlite')
curr = db.cursor()

curr.execute('DROP TABLE IF EXISTS Counts')

curr.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input("Enter file name: ")
if len(fname)< 1:
    fname = "mbox.txt"
data = open(fname, encoding="utf-8")

for line in data:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]

    org = email.split('@')[1]

    curr.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = curr.fetchone()

    if row is None:
        curr.execute('INSERT INTO Counts (org,count) VALUES (?, 1)',(org,))
    else:
        curr.execute('UPDATE Counts SET count=count+1 WHERE org = ?', (org,))
    
db.commit()

sqlstr = 'SELECT org,count FROM Counts ORDER BY count DESC LIMIT 10'

for line in curr.execute(sqlstr):
    print(str(line[0]), line[1])

curr.close()
db.close()