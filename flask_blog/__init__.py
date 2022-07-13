from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from flask_uploads import IMAGES,configure_uploads,UploadSet



app = Flask(__name__)

# Settings
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///users.db"
app.config['UPLOADED_IMAGES_DEST']="flask_blog/static/images"

# Database
db = SQLAlchemy(app)

# Configuring upload image
images=UploadSet("images",IMAGES)
configure_uploads(app,images)

# Salt for hashing
mySalt = bcrypt.gensalt()

# Importing forms
from flask_blog.forms import *

# Importing models
from flask_blog.models.blogModel import Blog
from flask_blog.models.userModel import User

# Importing routes
import flask_blog.routes.blog
import flask_blog.routes.users