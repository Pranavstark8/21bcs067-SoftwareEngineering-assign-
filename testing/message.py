# Import the required libraries
import mysql.connector
from flask import Flask, render_template, request

# Create a connection to the MySQL database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="@pranav007",
  database="ticket_bk"
)

# Create a Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Define the route for the form page
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Get the form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Insert the data into the database
        cursor = db.cursor()
        query = "INSERT INTO messages (name, email, message) VALUES (%s, %s, %s)"
        values = (name, email, message)
        cursor.execute(query, values)
        db.commit()
        
    return render_template('form.html')

# Define the route for the messages page
@app.route('/messages')
def messages():
    # Retrieve the data from the database
    cursor = db.cursor()
    query = "SELECT * FROM messages"
    cursor.execute(query)
    messages = cursor.fetchall()
    
    return render_template('messages.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
