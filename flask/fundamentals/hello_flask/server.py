from flask import Flask, render_template


app = Flask(__name__)



@app.route('/')
def hello_world():
    return render_template("index.html", phrase=hello, times=5)

@app.route('/say/<name>')
def say(name):
    return f"Hi {name}"

@app.route('/repeat/<int:num>/<word>')
def repeat(num,word):
    return (word * num)

@app.route('/dojo')
def success():
    return "Dojo!"


if __name__=="__main__":
    app.run(debug=True)