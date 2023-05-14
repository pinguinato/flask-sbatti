from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import date

app = Flask(__name__)
bootstrap=Bootstrap(app)

# my project's home page
@app.route("/")
def home_page(): 
    return render_template("index.html")


# route with a template parameters
@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


# route with templates with filters
@app.route("/user_with_filters/<name>")
def user_with_filters(name):
    string_to_trim = "  [ string to trim ]  "
    return render_template("user_with_filters.html", name=name, string_to_trim=string_to_trim)


# route with control structures
@app.route("/user_control_structure/<username>")
def user_control_structure(username):
    programming_language_list = ['Python', 'Java', 'Javascript', 'Sql', 'PHP', 'Ruby', 'Perl', 'Go']
    return render_template("user_control_structure.html", username=username, list=programming_language_list)


# route with use of blocks
@app.route("/blocks/<name>")
def use_of_blocks(name):
    date_of_the_day = date.today()
    return render_template("extended.html", name=name, date_of_the_day=date_of_the_day)


# route con Bootstrap
@app.route("/bootstrap/<name>")
def use_of_bootstrap(name):
    return render_template("page_with_bootstrap.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)