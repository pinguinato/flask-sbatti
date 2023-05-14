from flask import Flask, render_template

app = Flask(__name__)

# my project's home page
@app.route("/")
def home_page(): 
    return render_template("index.html")


# route with a template parameters
@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)



if __name__ == "__main__":
    app.run(debug=True)