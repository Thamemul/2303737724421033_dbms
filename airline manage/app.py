from flask import Flask, render_template, redirect, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'flight_app_key'

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'thamem007'  # Replace with your actual password
app.config['MYSQL_DB'] = 'flight_db'  # Update to your flight database name
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.htm')

@app.route('/flights')
def flights():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM flights")  # Query for flight data
    flight_info = cur.fetchall()
    cur.close()
    return render_template('flights.htm', flights=flight_info)

@app.route('/search_flight', methods=['POST', 'GET'])
def search_flight():
    search_results = []
    if request.method == "POST":
        search_term = request.form.get('flightid')
        cur = mysql.connection.cursor()
        query = "SELECT * FROM flights WHERE flight_id LIKE %s"
        cur.execute(query, ('%' + search_term + '%',))
        search_results = cur.fetchall()
        cur.close()
        return render_template('flights.htm', flights=search_results)

@app.route('/insert_flight', methods=['POST'])
def insert_flight():
    if request.method == "POST":
        flight_id = request.form.get('flightid')
        airline = request.form.get('airline')
        departure = request.form.get('departure')
        arrival = request.form.get('arrival')
        capacity = request.form.get('capacity')

        # Check if all fields are provided
        if not all([flight_id, airline, departure, arrival, capacity]):
            return render_template('flights.htm', error="All fields are required.")

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO flights (flight_id, airline, departure, arrival, capacity) VALUES (%s, %s, %s, %s, %s)",
                    (flight_id, airline, departure, arrival, capacity))
        mysql.connection.commit()
        return redirect(url_for('flights'))

@app.route('/delete_flight/<string:flight_id>', methods=['GET'])
def delete_flight(flight_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM flights WHERE flight_id=%s", (flight_id,))
    mysql.connection.commit()
    return redirect(url_for('flights'))

@app.route('/update_flight', methods=['POST', 'GET'])
def update_flight():
    if request.method == 'POST':
        flight_id = request.form.get('flightid')
        airline = request.form.get('airline')
        departure = request.form.get('departure')
        arrival = request.form.get('arrival')
        capacity = request.form.get('capacity')

        # Check if all fields are provided
        if not all([flight_id, airline, departure, arrival, capacity]):
            return render_template('flights.htm', error="All fields are required for update.")

        cur = mysql.connection.cursor()
        cur.execute("UPDATE flights SET airline=%s, departure=%s, arrival=%s, capacity=%s WHERE flight_id=%s",
                    (airline, departure, arrival, capacity, flight_id))
        mysql.connection.commit()
        return redirect(url_for('flights'))

if __name__ == "__main__":
    app.run(debug=True)
