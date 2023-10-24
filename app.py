from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    try:
        result = str(eval(expression))
    except Exception as e:
        result = 'Error'
    return render_template('index.html', result=result)


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
