from flask import Flask, render_template, request
import os
import json
import gspread
from google.oauth2.service_account import Credentials

# Google Sheets setup
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = '' #Enter your the name of your json file in the quotes

credentials = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

gc = gspread.authorize(credentials)
spreadsheet_id = '' #Enter your spreadsheet id which is after the /d in the url bar
worksheet = gc.open_by_key(spreadsheet_id).sheet1

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone = request.form['phone']

    # Append the data to the Google Sheet
    worksheet.append_row([first_name, last_name, email, phone])
    
    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
