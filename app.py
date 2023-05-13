from flask import Flask

app = Flask(__name__)

# my project's home page
@app.route("/")
def home_page():
    html_response = f"<h1>This is the Home Page</h1>" 
    return html_response

if __name__ == "__main__":
    app.run(debug=True)