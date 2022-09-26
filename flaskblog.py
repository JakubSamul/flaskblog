from turtle import title
from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "82kh76ni01o76su79kl07g9tg76kumd"

posts = [
    {
        "author": "Jakub Samul",
        "title": "Blog Flask 1",
        "content": "First post content",
        "date_posted": "September 26, 2022"
    },
    {
        "author": "Karol Dodo",
        "title": "Blog Flask 2",
        "content": "Second post content",
        "date_posted": "September 26, 2022"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/reginstert")
def reginster():
    form = RegistrationForm()
    return render_template("reginster.html", title="Reginster", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
