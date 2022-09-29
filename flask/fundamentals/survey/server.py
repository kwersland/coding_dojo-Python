from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secrets secrets"

# main page
@app.route("/")
def index():
    return render_template("index.html")

# processes form and redirects to /result
@app.route("/process", methods=["POST"]) 
def submit():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

# displays the filled out form
@app.route('/result')
def display():
    name = session['name']
    location = session['location']
    language = session['language']
    comment = session['comment']
    return render_template('result.html', name=name, location=location, language=language, comment=comment)

# resets the session and takes you back to the main page
@app.route('/restart', methods=["POST"])
def restart():
    session.clear() 
    return redirect('/')


if __name__ == "__main__":
    app.run(debug = True)