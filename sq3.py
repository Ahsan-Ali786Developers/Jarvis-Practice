import sqlite3 as sq 

conn  = sq.connect("user.db")

cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,Username TEXT NOT NULL,Password TEXT NOT NULL)''')
conn.commit()

print("Table created successfully")

def add_user(username, password):
    cursor.execute("INSERT INTO users (Username, Password) VALUES (?, ?)", (username, password))
    conn.commit()
    print("User added successfully")
def check_user(username, password):
    cursor.execute("SELECT * FROM users where Username =? and Password = ?",(username, password))
    user = cursor.fetchone() 
    if user:
        return True
    else:
        return False
   

if check_user("jon", "pas23"):
    print("User Exists")
else:
    print('User does not exist. So, we are adding a new user')
    add_user("jon", "pas23")
