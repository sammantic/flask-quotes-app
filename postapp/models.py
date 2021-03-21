from postapp import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(20), nullable=True)
    like = db.Column(db.Integer, nullable=True)
    dislike = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"Post('{self.post}', '{self.like}', '{self.dislike}')"