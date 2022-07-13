from flask_blog import app,NewBlogForm,db,Blog
from flask import render_template,request,redirect,g
from datetime import date


# Home
@app.route("/")
def index():
    args=request.args
    sort=args.get("sort",default="oldest")
    posts=Blog.query.order_by(Blog.date)
    if sort == "oldest":
        posts=Blog.query.order_by(Blog.date)
    elif sort == "latest":
        posts=Blog.query.order_by(Blog.date.desc())
    elif sort == "alphabetically":
        posts = Blog.query.order_by(Blog.title)
    return render_template('home.html',posts=posts,title="Home",sort=sort)

# Single blog page
@app.route("/<int:id>")
def blog_get(id):
    post = Blog.query.filter_by(id=id).first()
    return render_template('blog.html',post=post,title=post.title)

# New blog page
@app.route("/new_blog",methods=["POST","GET"])
def new_blog():
    form=NewBlogForm()
    method=request.method
    # If blog is successfully created
    if method == "POST" and form.validate():
        title=form.title.data
        text=form.text.data
        blog=Blog(title=title,text=text,user_id=g.user.id,date=date.today())
        db.session.add(blog)
        db.session.commit()
        return redirect("/")
    return render_template("new_blog.html",title="New Blog",form=form)

# Delete blog
@app.route("/delete/<int:id>",methods=["GET","POST"])
def delete_blog(id):
    method=request.method
    post=Blog.query.filter_by(id=id).first()
    if not post or post.user.id!=g.user.id:
        return redirect("/")
    if method == "POST":
        db.session.delete(post)
        db.session.commit()
        return redirect("/")
    return render_template("delete_blog.html",title="Delete Blog",post=post)

# Edit blog
@app.route("/edit_blog/<int:id>",methods=["GET","POST"])
def edit_blog(id):
    method=request.method
    post=Blog.query.filter_by(id=id).first()
    form=NewBlogForm(title=post.title,text=post.text)
    if not post or post.user.id!=g.user.id:
        return redirect("/")
    if method == "POST":
        post.title=form.title.data
        post.text=form.text.data
        db.session.commit()
        return redirect("/")
    return render_template("edit_blog.html",title="Edit Blog",post=post,form=form)
