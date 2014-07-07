from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/hello')
def hello_again():
    return render_template('hello.html')

@app.route('/hi/<name>')
def hello_with_variables(name):
    return render_template('hi.html', name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
