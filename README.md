# Intro_page
Web page. There is a form with a name entry field. If name us unique system adds this user to the database, and redirects him to the page with the greetings message. If user's name is not unique, system reminds him about registration. There also a link with a list of everyone you have already greeted. 

# Flask
Flask is a framework for building web applications in the Python programming language using the Werkzeug toolkit and the Jinja2 templating engine.

# Installation
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
SQLite is relational database management system (RDBMS) contained in a C library. 
In contrast to many other database management systems, SQLite is not a client–server database engine.

-sudo apt install sqlite3

in the application (main.py):
import sqlite3

# Steps with commands for creating table "NAMES":
1.source venv/bin/activate
2.sqlite3 names
3.CREATE TABLE NAMES(ID integer primary key autoincrement, Name varchar(200));

(varchar is a data type similar to text, the only difference is that
the text takes up about is designed for large volumes of text and takes
a lot of space in the database, but if you know that the data in the column will be
not very large for example Name, then you can use varchar
indicating the maximum column size, in this example 200)

# Detailed analysis of the main page execution:

<p> @app.route('/') </p>
<p> @app.route('/add', methods=['GET', 'POST'])</p>
<p> def get_title():</p>
    
