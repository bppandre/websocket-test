from flask import Flask, request


app = Flask(__name__)
app.config["DEBUG"] = True

resultData = []

@app.route('/', methods=["GET"])
def home():
    return str(resultData)


def suma(array):
    res = 0
    for i in array:
        res += i
    return res

@app.route('/result', methods=["GET"])
def result():
    return str(suma(resultData))

@app.route('/submit', methods=["POST"])
def add():
    if request.method == 'POST':
        client_number = request.form['number']
        resultData.append(int(client_number))
        return str('Number Received')


app.run()