from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import date
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap=Bootstrap(app)
moment=Moment(app)
app.config['SECRET_KEY']='38d0776e0970b72f85140f2ca6f2d5'

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


# error page 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# pagina con la favicon
@app.route("/favicon")
def favicon():
    return render_template("favicon.html", current_time=datetime.utcnow())

# definizione di una classe per il form
class NameForm(FlaskForm):
    name = StringField('What is you name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
    


# rotta con un form
@app.route("/form_esempio", methods=['GET', 'POST'])
def form_esempio():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template("pagina_con_form.html", form=form, name=name)
    



if __name__ == "__main__":
    app.run(debug=True)