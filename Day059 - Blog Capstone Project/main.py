from flask import Flask, render_template, request
import requests
from post import Post


blog_url = "https://api.npoint.io/eb6cd8a5d783f501ee7d"
response = requests.get(blog_url, verify=False)
all_posts = response.json()
post_objects=[]
for post in all_posts:
    post_obj = Post(post["id"],post["title"],post["subtitle"],post["author"], post["body"],post["image_url"], post["image_alt"], post["date"])
    post_objects.append(post_obj)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts = post_objects)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == "GET":
        return render_template("contact.html", contact=False)
    else:
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        print(name)
        print(email)
        print(phone)
        print(message)
        return render_template("contact.html", contact=True)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template('post.html',post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)