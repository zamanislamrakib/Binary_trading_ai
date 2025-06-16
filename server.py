from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="🚀 Binary Trading AI Server Running")

if __name__ == '__main__':
    app.run(debug=True)
