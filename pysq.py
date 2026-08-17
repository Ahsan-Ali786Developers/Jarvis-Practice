# forgot exact syntax
import pymysql as sq

conn = sq.connect(host="localhost", user='root', password='0000', database='testdb')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXIsTS users(id Int primary key auto_increment not null, username Text not null, password text not null)""")
conn.commit()
print("table is created successfully!")

def add_user(username, password):
    cursor.execute("""INSERT INTO users (username, password) Values (%s , %s)""",(username, password))
    conn.commit()
def check_user(username, password):
    cursor.execute("""Select * from users where username=%s and password=%s """,(username, password))
    user = cursor.fetchone()
    if user:
        return True
    else: 
        return False
if check_user('Ali', '1@25'):
    print("user existed!")
else:
    print("User is not existed. So, we are adding...")
    add_user("Ali", "1@25")
