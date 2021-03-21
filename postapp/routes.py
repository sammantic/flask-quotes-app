from flask import render_template
from postapp import app
from postapp.models import Post

@app.route("/")
def index():
    all_post = Post.query.all();
    print(all_post[0].post)
    return render_template("post.html", posts=all_post)

@app.route("/like", methods=['GET', 'POST'])
def like():
    pass

@app.route("/dislike", methods=['GET', 'POST'])
def dislike():
    pass
