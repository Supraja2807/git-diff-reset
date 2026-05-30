from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask Application"

@app.route('/health')
def health():
    return jsonify({
        "status": "UP",
        "application": "Flask Demo"
    })

@app.route('/user/<name>')
def user(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=false)
