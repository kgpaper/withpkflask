from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/home", methods=['GET','POST'])
def home():
    return render_template('onsurvey.html')

@app.route("/", methods=['GET','POST'])
def example():
    return render_template('example.html')

if __name__ == "__main__":
    app.run(port = 8000)