from flask import Flask, render_template, request, jsonify
from predictor import predict

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def formpage():
    if (request.method == 'POST'):
        data = request.json
        data2 = [float(value) for value in data.values()]
        result = predict((*data2))
        responsetosend = jsonify(result)
        return responsetosend
    else :
        return render_template('index.html')
