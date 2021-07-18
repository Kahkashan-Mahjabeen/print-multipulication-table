# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#   return '<h1>Helllo World!</h1>'

# if __name__ == '__main__':
#   app.run()

from flask import Flask, render_template
app = Flask(__name__)
app.debug = True
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculator')
def home():
    return render_template('calculator.html')



if __name__ == '__main__':
    app.run()
