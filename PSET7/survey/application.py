import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")

# Writes to csv file based on "Name=" attributes in form.html
@app.route("/form", methods=["POST"])
def post_form():
    if not request.form.get("Name") or not request.form.get("color") or not request.form.get("difficulty") or not request.form.get("food"):
        return render_template("error.html")
    file = open("survey.csv", "a")
    writer = csv.writer(file)
    writer.writerow((request.form.get("Name"), request.form.get("color"), request.form.get("difficulty"), request.form.get("food")))
    file.close()
    return redirect("/sheet")

# Loads/Reads csv and sends to template in table.html
@app.route("/sheet", methods=["GET"])
def get_sheet():
    file = open("survey.csv", "r")
    reader = csv.reader(file)
    results = list(reader)
    file.close()
    return render_template("table.html", results=results)