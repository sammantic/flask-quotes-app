from flask import Flask, render_template
from flask_sqlalchemy  import SQLAlchemy


app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

from models import Post
@app.route("/")
def index():
    return render_template("post.html")

if __name__ == "__main__":
    app.run(debug=True)