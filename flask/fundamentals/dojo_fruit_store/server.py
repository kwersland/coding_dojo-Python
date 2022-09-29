from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secrets secrets"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    session['name'] = request.form['name']
    session['id'] = request.form['id']
    return redirect('/checkout')

@app.route('/checkout')
def display():
    name = session['name']
    id = session['id']
    return render_template('checkout.html', name=name, id=id)

if __name__ == '__main__':
    app.run(debug = True)