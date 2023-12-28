from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

'''
home route
'''


@app.route("/")
def home():
    return render_template("index.html")


'''
improving the code with dynamic url
'''


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


'''
saving form data into a txt file
'''


def save_to_file(data):
    with open("database.txt", mode="a") as file:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file.write(f"\n{email},{subject},{message}")


'''
saving form data into a csv file
'''


def save_to_csv_file(data):
    with open("database.csv", mode="a", newline="") as file:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(file, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


'''
route for submit form
'''


@app.route("/submit_form", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            save_to_file(data)
            save_to_csv_file(data)
            return redirect("thankyou.html")
        except :
            return "cannot save to the database"
    else:
        return "something went wrong"


'''
improving the code with dynamic url
'''
# @app.route("/about.html")
# def about():
#     return render_template("about.html")
#
#
# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")
#
#
# @app.route("/work.html")
# def work():
#     return render_template("work.html")
#
#
# @app.route("/works.html")
# def works():
#     return render_template("works.html")
#
#
