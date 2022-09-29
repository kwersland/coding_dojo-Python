from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello World!</h1>"

@app.route('/play')
def play():
    return render_template("playground.html", x=3, color="lightblue")

@app.route('/play/<int:x>')
def play_x(x):
    return render_template("playground.html", x=x, color="lightblue")

@app.route('/play/<int:x>/<color>')
def play_color(x,color):
    return render_template("playground.html", x=x, color=color)

if __name__=="__main__":
    app.run(debug=True)