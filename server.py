from flask import Flask, render_template, url_for, request, redirect
import os
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    try:
        return render_template(page_name)
    except Exception:
        return render_template('/404.html')


def db(data):
    if os.path.isfile('database.txt'):
        with open('database.txt', 'a') as db:
            email = data['email']
            subject = data['subject']
            msg = data['message']
            db.write(f'\n{email}\t\t\t{subject}\t\t\t{msg}\t\t\t')


def db_csv(data):
    if os.path.isfile('database.csv'):
        with open('database.csv', 'a') as db:
            email = data['email']
            subject = data['subject']
            msg = data['message']
            csv_writer = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([email, subject, msg])


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        # db(data)
        db_csv(data)
        return redirect("/thankyou.html")
    else:
        return redirect("/sww.html")
