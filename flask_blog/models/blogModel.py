from flask_blog import db
from datetime import date

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.Date, default=date.today())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Blog<{self.title},{self.id}>"