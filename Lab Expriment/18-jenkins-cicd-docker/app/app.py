from flask import Flask, jsonify
app = Flask(__name__)
def add(a, b): return a + b
@app.get("/")
def home(): return jsonify(message="CI/CD demo", sum=add(2, 3))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
