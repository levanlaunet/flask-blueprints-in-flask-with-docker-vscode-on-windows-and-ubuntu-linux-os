from flask import Blueprint, render_template
app1 = Blueprint('app1', __name__, template_folder="templates/app1", static_folder='static')

@app1.route("/")
def home():
    return render_template('index.app1.html')