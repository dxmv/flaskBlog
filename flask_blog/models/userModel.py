from flask_blog import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(60), unique=True, nullable=False)
    picture = db.Column(db.String(1000), unique=True, default="default.jpg")
    blogs = db.relationship("Blog", backref="user", lazy=True)

    def __repr__(self):
        return f"User<{self.username},{self.email}>"