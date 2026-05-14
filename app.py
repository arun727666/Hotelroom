from flask import Flask, render_template, request, redirect, url_for
import json
import os
import urllib.request
import urllib.error
from datetime import datetime

app = Flask(__name__)

def load_rooms():
    with open('data/rooms.json', 'r') as f:
        return json.load(f)

#start-1
@app.route('/')
def index():
    rooms = load_rooms()
    # Feature top 3 rooms
    featured_rooms = rooms[:3]
    return render_template('index.html', featured_rooms=featured_rooms)

@app.route('/rooms')
def rooms():
    rooms_data = load_rooms()
    return render_template('rooms.html', rooms=rooms_data)

@app.route('/book/<int:room_id>')
def book(room_id):
    rooms_data = load_rooms()
    room = next((r for r in rooms_data if r['id'] == room_id), None)
    if not room:
        return redirect(url_for('rooms'))
    return render_template('booking.html', room=room)

@app.route('/confirm', methods=['POST'])
def confirm():
    if request.method == 'POST':
        booking_details = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'checkin': request.form.get('checkin'),
            'checkout': request.form.get('checkout'),
            'room_name': request.form.get('room_name'),
            'price': request.form.get('price'),
            'total': request.form.get('total'), # In a real app, calculate backend side
            'booking_id': f"BKG-{int(datetime.now().timestamp())}"
        }
        
        # Send to Google Sheets
        GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbw5spfpd6dSdR0EJjFenbIIIH3TYZY_kRb2OxLqPmCm2zegyYhj7P-lWAHKsADoJzEy2Q/exec"
        try:
            req = urllib.request.Request(GOOGLE_SCRIPT_URL)
            req.add_header('Content-Type', 'application/json')
            jsondata = json.dumps(booking_details).encode('utf-8')
            req.add_header('Content-Length', len(jsondata))
            response = urllib.request.urlopen(req, jsondata)
        except Exception as e:
            print(f"Error sending to Google Sheets: {e}")

        return render_template('confirmation.html', booking=booking_details)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
