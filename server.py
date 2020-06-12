from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
@app.route('/<string:url>')
def my_url(url=None):
    if url != None:
        try:
            return render_template(url)
        except:
            print('The requested url does not exist!')
    return render_template('index.html')


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'Email: {email}, Subject: {subject}, Message: {message}\n')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            write_to_file(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'something went wrong'
