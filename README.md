# Intro_page
==================
Web page. There is a form with a name entry field. If name us unique system adds this user to the database, and redirects him to the page with the greetings message. If user's name is not unique, system reminds him about registration. There also a link with a list of everyone you have already greeted. 

# Flask
==================
Flask is a framework for building web applications in the Python programming language using the Werkzeug toolkit and the Jinja2 templating engine.

## Installation
==================
1.sudo virtualenv venv
2.source venv/bin/activate
3.sudo pip3 install Flask

in the application (main.py):

from flask import Flask
app = Flask(__name__)
app.run(debug=True, port=5002)

"""
Best server run app.run (debug = True)
insert into if __name__ == '__main__' conditions:
this is necessary so that this file does not start the server
if you import this file from another python file
"""

# SQLite
==================
SQLite is relational database management system (RDBMS) contained in a C library. 
In contrast to many other database management systems, SQLite is not a client–server database engine.

-sudo apt install sqlite3

in the application (main.py):
import sqlite3

## Steps with commands for creating table "NAMES":
======================================================
1.source venv/bin/activate
2.sqlite3 names
3.CREATE TABLE NAMES(ID integer primary key autoincrement, Name varchar(200));

(varchar is a data type similar to text, the only difference is that
the text takes up about is designed for large volumes of text and takes
a lot of space in the database, but if you know that the data in the column will be
not very large for example Name, then you can use varchar
indicating the maximum column size, in this example 200)

## Detailed analysis of the main page execution:
======================================================

@app.route('/')
@app.route('/add', methods=['GET', 'POST'])
def get_title():
    if request.method == 'GET':
    
    *"""
    if the user just opened the page, he sent a get request to the server. 
    form is needed to get info and send it later through post request
    """*

        response = make_response(render_template('add.html'))
    elif request.method == 'POST':
        tittle = request.form['Name']
        if not tittle:
            return "Будь ласка, вкажіть ім'я!"
            
            
        connection = sqlite3.connect("names")
        *# Connect to database
        
        cursor = connection.cursor()
        *# Initialize the cursor to perform operations*
        
        cursor.execute("SELECT * FROM NAMES WHERE Name = ( ? )", (tittle,))
        *# checking if name was alredy in the database. (any SQL commands can be inserted in the execute method)*
        
        result = cursor.fetchall()
        *# Next, to retrieve the result of the SELECT command, use the fetchall method*

        if not result:
        *# As the name from a form was not in the database, redirecting user to the page with the greetings.* 
        
            cursor.execute("""INSERT INTO NAMES ( Name ) VALUES ( ? )""", (tittle,))
            *# Adding new name into the database*
            
            connection.commit()
            *#In cases where we create a table, add a record, update a record, delete a record
            and all other operations that require execution, they must be sent to the database for execution
            for this we use the commit () method in the connection*
            
            connection.close()
            *# Be sure to close the connection*
            
            response = redirect("/hello")
            *# Redicecting to the page with the greetings*

        else:
        *# Redicecting to the page which reminds user that he has alredy added his name into the database*
            connection.commit()
            connection.close()
            response = make_response(
                render_template('old.html', tittle=tittle))


    return response

