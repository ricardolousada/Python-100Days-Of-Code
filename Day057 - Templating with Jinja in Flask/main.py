from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

def get_gender(name):
    url = f"https://api.genderize.io?name={name}"
    response = requests.get(url, verify=False)
    data = response.json()
    gender = data['gender']
    print(gender)
    return gender

def get_age(name):
    url = f"https://api.agify.io?name={name}"
    response = requests.get(url, verify=False)
    data = response.json()
    #print(data)
    age = data['age']
    print(age)
    return age



@app.route('/')
def home():
    year = datetime.date.today().year
    random_number = random.randint(1,10)
    return render_template('index.html',num=random_number, year=year)

@app.route('/guess/<username>')
def show_user_profile(username):
    gender = get_gender(username)
    age = get_age(username)
    name = str(username).capitalize()
    return render_template('age_and_gender.html',name=name,gender=gender, age=age)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url,verify=False)
    all_posts = response.json()
    return render_template('blog.html', posts = all_posts)


if __name__ == "__main__":
    app.run(debug=True)


