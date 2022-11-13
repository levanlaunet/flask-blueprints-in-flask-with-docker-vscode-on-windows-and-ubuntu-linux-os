from flask import Blueprint, render_template
app2 = Blueprint('app2', __name__, template_folder="templates/app2")

@app2.route("/")
def home():
    return render_template('index.app2.html')