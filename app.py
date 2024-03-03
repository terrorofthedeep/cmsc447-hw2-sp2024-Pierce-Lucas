from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

import sqlite3

app = Flask(__name__)


#Home page/index
@app.route("/")
def home():
    return redirect(url_for("display"))

@app.route("/display")
def display():
    #displays the current database
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT rowid, * FROM people")

    rows = cursor.fetchall()
    connection.close()

    return render_template("display.html", rows = rows)

@app.route("/deletePerson", methods=["POST","GET"])
def deletePerson():
    #display.html passes the person's ID
    if request.method == 'POST':
        id = request.form['id']

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute("DELETE FROM people WHERE id = (?)", (id,))
        connection.commit()
        connection.close()
    else:
        print("Error in deletePerson()")
    return redirect(url_for("display"))


@app.route("/editPerson", methods=["POST", "GET"])
def editPerson():
    #display.html passes the new name, id, and points
    
    if request.method == "POST":
        #Get variables from the form in display.html
        name = request.form['newName']
        id = request.form['newID']
        points = request.form['newPoints']
        rowid = request.form['rowid']
        
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        #We use the row # to identify people rather than ID, bc we might be changing id
        cursor.execute("UPDATE people SET name='"+name+"', id='"+id+"', points='"+points+"' WHERE rowid="+rowid)
        connection.commit()
        connection.close()
    return redirect(url_for("display"))
    