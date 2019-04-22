from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('base.html')

@app.route('/')
def hello1():
    return "Rishabh"

if __name__ == '__main__':
    app.run(debug=True)
