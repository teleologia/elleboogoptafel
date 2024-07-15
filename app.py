# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/bereken_scores', methods=['POST'])
def bereken_scores():
    data = request.json
    spelers = data['spelers']
    biedingen = data['biedingen']
    slagen = data['slagen']
    ronde_nummer = data['rondeNummer']

    scores = []
    for i in range(len(spelers)):
        if biedingen[i] == slagen[i]:
            score = 10 + slagen[i] * 3  # Updated scoring rule
        else:
            score = -3 * abs(biedingen[i] - slagen[i])
        scores.append(score)

    return jsonify(scores=scores)


if __name__ == '__main__':
    app.run(debug=True)