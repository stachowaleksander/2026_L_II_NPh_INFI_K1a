from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    # Poprawny format JSON i imię Aleksander
    return jsonify({"imie": "Aleksander", "wiadomosc": "Simple Flask App działa!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)