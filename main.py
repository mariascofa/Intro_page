from flask import Flask, render_template, request, make_response, redirect
import sqlite3

app = Flask(__name__)


# Steps with commands for creating table "NAMES":
# 1.source venv/bin/activate
# 2.sqlite3 names
# 3.CREATE TABLE NAMES(ID integer primary key autoincrement, Name varchar(200));

@app.route('/show')
def show():
    """This page will display list with names and IDs of all the users, who have already put name in the system."""
    connection = sqlite3.connect("names")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM NAMES")
    fields = cursor.fetchall()
    connection.close()
    return render_template('show.html', fields=fields)


@app.route('/hello')
def hello():
    """This page will display greetings message with the name of the person,
    if his name hasn't been added into the database before."""
    connection = sqlite3.connect("names")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM NAMES WHERE id = (SELECT MAX(id) FROM NAMES)")
    fields = cursor.fetchall()
    connection.close()
    return render_template('hello.html', fields=fields)


@app.route('/')
@app.route('/add', methods=['GET', 'POST'])
def get_title():
    """This page will accept two types of GET and POST requests. When user open this page it shows
    form for entering name. If name hasn't been added into the database before, system adds this user to the database,
    and redirects him to the page with the greetings message.
    If user's name is not unique, it redirects him to the page that reminds him that he has already put his
    name into the system."""
    if request.method == 'GET':
        response = make_response(render_template('add.html'))
    elif request.method == 'POST':
        tittle = request.form['Name']
        if not tittle:
            return "Будь ласка, вкажіть ім'я!"
        connection = sqlite3.connect("names")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM NAMES WHERE Name = ( ? )", (tittle,))
        result = cursor.fetchall()
        print(result)

        if not result:
            cursor.execute("""INSERT INTO NAMES ( Name ) VALUES ( ? )""", (tittle,))
            connection.commit()
            connection.close()
            response = redirect("/hello")

        else:
            connection.commit()
            connection.close()
            response = make_response(
                render_template('old.html', tittle=tittle))

    return response


if __name__ == '__main__':
    app.run(debug=True, port=5002)
