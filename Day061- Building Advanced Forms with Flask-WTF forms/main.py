from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'well-secret-password'
bootstrap = Bootstrap5(app)

class MyForm(FlaskForm):
    invalid_email = "Invalid email address"
    invalid_password = "Field must be at least 8 characters long."
    email = StringField(label='Email', validators=[DataRequired(message=invalid_email), Email(message=invalid_email)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(message=invalid_password, min=8)])
    button = SubmitField(label='Log In')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET","POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print(email)
        print(password)
        if (email == "admin@email.com") and (password == "12345678"):
            print("Entrei no sucess")
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
