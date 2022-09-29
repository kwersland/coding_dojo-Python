from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secrets secrets"

@app.route("/")
def index():
    if "count" not in session:
        session['count'] = 1
    else:
        session['count'] +=1
    return render_template("index.html")

@app.route('/reset')
def restart():

    del session['count']
    return redirect('/')


if __name__ == '__main__':
    app.run(debug = True)