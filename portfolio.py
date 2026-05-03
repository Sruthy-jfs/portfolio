import csv
from shlex import quote

from flask import Flask, render_template, request, redirect

print("🔥 THIS FILE IS RUNNING")

app = Flask(__name__)

@app.route('/') #its a decorator. It tells everytime we encounter '/'(root) I want you to define a function
def my_home():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('./database.txt', 'a') as database:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        file=database.write(f'{email},{subject},{message}\n')



def write_to_csv(data):
    with open('./database.csv', 'a', newline='') as database2:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer=csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data=request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong. Try again later!'


print(app.url_map)