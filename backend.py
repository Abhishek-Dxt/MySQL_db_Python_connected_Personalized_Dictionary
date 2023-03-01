import mysql.connector
import random

con = mysql.connector.connect(
user = "root",
password = "******",
host = "127.0.0.1",
database = "entries",
port = "3306"
    )

def mydict(raw_word):    
    word = raw_word.capitalize()
    mycursor = con.cursor()
    query = mycursor.execute("select meaning from entries where word = '%s'" % word)
    results = mycursor.fetchall()
    c = []
    for result in results:
        c.append(result[0])
    return c

def status(raw_word):
    word = raw_word.capitalize()
    mycursor = con.cursor()
    query = mycursor.execute("select status from entries where word = '%s'" % word)
    results = mycursor.fetchall()
    if results[0][0] == None:
        return "---"
    else:
        return results[0][0]

def update(raw_word):
    word = raw_word.capitalize()
    mycursor = con.cursor()
    query = mycursor.execute("update entries set status='imp' where word = '%s'" % word)
    con.commit()

def bonus():
    mycursor = con.cursor()
    mycursor.execute("select word from entries where status = 'imp'")
    i_list = mycursor.fetchall()
    imp_list = [i[0] for i in i_list]
    global bonus_word
    bonus_word = random.choice(imp_list)
    return mydict(bonus_word)
