from flask import Flask, render_template, request, redirect
import csv
# instantiate app from FLASK class
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('./index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    # mode='a' is to append
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')
    # database.close()


def write_to_csv(data):
    # mode='a' is to append
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        # config, location, what character as delimiter, quotation marks
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])



# request method allows sending/receiving data
# get browser wants to send info, post browser wants to save info
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # return 'form submitted'
    if request.method == 'POST':
        try:
            # data = request.form['message']
            # convert info into dict - grabs all data with fields
            data = request.form.to_dict()
            # print(data)
            # write_to_file(data)
            write_to_csv(data)

            # return 'form submitted'
            return redirect('/thankyou.html')
        except:
            return 'data not save in database'

    # if not POST method then:
    else:
        return 'Are you unable to correctly fill out a form?'

    # to run in cmd = set FLASK_APP=file.py
    # set FLASK_ENV=development, flask run