from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "No secrets on github or youtube"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    print(request.form)
    session['name'] = request.form['name']
    session['age'] = request.form['age']
    return redirect('/display')

@app.route('/display')
def display():
    name = session['name']
    return render_template('display.html', name=name, age=submit['age'])

if __name__ == '__main__':
    app.run(debug = True)