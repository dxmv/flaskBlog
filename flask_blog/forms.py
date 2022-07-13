from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,PasswordField,EmailField,FileField
from wtforms.validators import DataRequired,Length,EqualTo,Email
from flask_wtf.file import FileAllowed

# New blog form with title and text fields
class NewBlogForm(FlaskForm):
    title=StringField(label="Title",validators=[DataRequired(),Length(8,25)])
    text=TextAreaField(label="Text",validators=[DataRequired(),Length(50)])

# Login form with username and password
class LoginForm(FlaskForm):
    username=StringField(label="Username:",validators=[DataRequired()])
    password=PasswordField(label="Password",validators=[DataRequired()])

# Register form with all required field for user
class RegisterForm(FlaskForm):
    username = StringField(label="Username:",validators=[DataRequired(),Length(4,25)])
    email = EmailField(label="Email",validators=[DataRequired(),Email()])
    password=PasswordField(label="Password",validators=[DataRequired()])
    confirm_password = PasswordField(label="Confirm Password", validators=[DataRequired(),EqualTo("password")])
    picture = FileField(label="Image",validators=[FileAllowed(['jpg', 'png'])])

# Edit profile form without profile picture
class EditForm(FlaskForm):
    username = StringField(label="Username:",validators=[DataRequired(),Length(4,25)])
    email = EmailField(label="Email",validators=[DataRequired(),Email()])
    password=PasswordField(label="Password",validators=[DataRequired()])

# Edit profile picture form
class EditPicture(FlaskForm):
    picture = FileField(label="Image", validators=[FileAllowed(['jpg', 'png'])])
