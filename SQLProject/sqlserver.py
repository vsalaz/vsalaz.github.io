import mysql.connector as mq
from mysql.connector import errorcode

def server_connect():
    try: 
        conn = mq.connect(
            host = "localhost",
            user = "root",
            passwd = "Beba2394"
        )
        print("Connected to mySQL")
    except mq.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        print("Connection closed")
    conn.close()

#server_connect()

# connect to database
conn = mq.connect(host='localhost',user='root',password='Beba2394',db='menagerie')
c = conn.cursor()  # cursor to perform operations

def show_databases():
    show ="show databases"
    c.execute(show)
    print(f'------------')
    for show in c:
        print(f'{show[0]}')
    print(f'------------')

#show_databases()

def drop_db():
    c.execute("DROP DATABASE IF EXISTS menagerie")

#drop_db()

def create_db():
    c.execute("CREATE DATABASE menagerie")
    show_databases()

#create_db()

def create_table():
    c.execute("USE menagerie")
    c.execute("CREATE TABLE pet(name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), birth DATE, death DATE);")
    desc = "DESCRIBE pet"
    c.execute(desc)
    for desc in c: 
        print(f'{desc}') # prints out the structure of the table

#create_table()

def insert_data():
    c.execute("USE menagerie")
    c.execute("INSERT INTO pet (name,owner,species,sex,birth,death) VALUES \
    ('Fluffy','Harold', 'cat', 'f','1993-02-04',NULL),\
    ('Claws','Gwen', 'cat', 'm','1994-03-17',NULL),\
    ('Buffy','Harold', 'dog', 'f','1989-05-13',NULL),\
    ('Fang','Benny', 'dog', 'm','1990-08-27',NULL),\
    ('Bowser','Diane', 'dog', 'm','1979-08-31','1995-07-29'),\
    ('Chripy','Gwen', 'bird', 'f','1998-09-11',NULL),\
    ('Whistler','Gwen', 'bird', NULL ,'1997-12-09',NULL),\
    ('Slim','Benny', 'snake', 'm','1996-04-29',NULL),\
    ('Puffball','Diane', 'hamster', 'f','1999-03-30',NULL)")
    conn.commit()
    c.execute("SELECT * FROM pet")
    for tb in c:
        print(tb)

#insert_data()

def fdog_query():
    c.execute("SELECT * FROM pet WHERE sex = 'f' AND species ='dog'")
    for i in c:
        print(i[0], i[1], i[2], i[3], i[4], i[5])
#fdog_query() 

def pet_birth():
    c.execute("SELECT name, birth FROM pet")
    for i in c:
        print(i[0], i[1])
#pet_birth()

def pet_owners():
    c.execute("SELECT owner, COUNT(*) FROM pet GROUP BY owner")
    for i in c:
        print(i[0], i[1])
#pet_owners()

def pet_month():
    c.execute("SELECT name, birth, MONTH(birth) FROM pet")
    for i in c:
        print(f'{i[0]}\t{i[1]}\t{i[2]}')
pet_month()