from flask_blog import app,db,User,images,mySalt,LoginForm,RegisterForm,EditForm,EditPicture
from flask import render_template,request,redirect,session,g
import bcrypt

# Get the current user if it exists
@app.before_request
def get_user():
    if "user_id" in session:
        g.user = User.query.filter_by(id=session["user_id"]).first()


# User login
@app.route("/login",methods=["GET","POST"])
def login():
    form=LoginForm()
    method=request.method
    if method == "POST" and form.validate():
        session.pop("user_id",None)
        username=form.username.data
        password=form.password.data
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password):
            session["user_id"] = user.id
            return redirect("/")
        return redirect("/login")
    return render_template("login.html",title="Login",form=form)

# User register
@app.route("/register",methods=["GET","POST"])
def register():
    form=RegisterForm()
    method=request.method
    if method == "POST" and form.validate():
        username=form.username.data
        password=form.password.data
        email=form.email.data
        filename=""
        if form.picture.data:
            filename = images.save(form.picture.data)
        hash = bcrypt.hashpw(password.encode("utf-8"), mySalt)
        if filename!="":
            u = User(username=username, password=hash, email=email, picture=filename)
        else:
            u = User(username=username, password=hash, email=email)
        if hash:
            db.session.add(u)
            db.session.commit()
        return redirect("/")
    return render_template("register.html",title="Register",form=form)

# Profile view
@app.route("/profile/<int:id>")
def profile(id):
    user = User.query.filter_by(id=id).first()
    if not user:
        return redirect("/")
    return render_template("profile.html",user=user)

# Logout
@app.route("/logout")
def logout():
    if not g.user:
        return redirect("/login")
    session.pop("user_id",None)
    return redirect("/login")

# Edit profile picture
@app.route("/edit_picture/<int:id>",methods=["GET","POST"])
def edit_picture(id):
    user=User.query.filter_by(id=id).first()
    form=EditPicture(picture=user.picture)
    if not user:
        return redirect("/login")
    if user.id!=g.user.id:
        return redirect("/")
    if request.method=="POST" and form.validate():
        filename = images.save(form.picture.data)
        user.picture=filename
        db.session.commit()
        return redirect(f"/profile/{user.id}")
    return render_template("edit_picture.html",form=form)

# Edit profile
@app.route("/edit_user/<int:id>",methods=["GET","POST"])
def edit_profile(id):
    user=User.query.filter_by(id=id).first()
    form=EditForm(username=user.username,email=user.email)
    method=request.method
    if not user:
        return redirect("/login")
    if user.id!=g.user.id:
        return redirect("/")
    if method == "POST" and form.validate():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        filename = ""
        hash = bcrypt.hashpw(password.encode("utf-8"), mySalt)
        if hash:
            user.username=username
            user.email=email
            db.session.commit()
        return redirect(f"/profile/{user.id}")
    return render_template("edit_user.html",form=form)
