from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("checkerboard.html", x=8, y=8, color1="red", color2="black")

@app.route('/4')
def play_x():
    return render_template("checkerboard.html", x=8, y=4, color1="red", color2="black")

@app.route('/<int:x>/<int:y>')
def play_size(x,y):
    return render_template("checkerboard.html", x=x, y=y, color1="red", color2="black")

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def play_color(x,y,color1,color2):
    return render_template("checkerboard.html", x=x, y=y, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)
