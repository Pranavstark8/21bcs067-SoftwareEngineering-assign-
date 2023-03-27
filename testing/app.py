from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Set up the database connection
cnx = mysql.connector.connect(
    user='root',
    password='@pranav007',
    host='localhost',
    database='ticket_bk'
)

# Set up the database cursor
cursor = cnx.cursor()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form', methods=['POST'])
def form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    query = "INSERT INTO messages (name, email, message) VALUES (%s, %s, %s)"
    values = (name, email, message)
    cursor.execute(query, values)
    cnx.commit()
     #print("aaaa")
    return redirect(url_for('home'))


@app.route('/messages')
def messages():
    cursor.execute("SELECT * FROM messages")
    messages = cursor.fetchall()
    return render_template('messages.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
