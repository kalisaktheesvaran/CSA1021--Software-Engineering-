from flask import Flask, jsonify, request
app = Flask(__name__)
tasks = [{"id": 1, "title": "Learn Docker", "done": False}]

@app.get("/")
def home(): return jsonify(message="Flask API running in a container", status="ok")

@app.get("/health")
def health(): return jsonify(status="healthy")

@app.get("/tasks")
def list_tasks(): return jsonify(tasks)

@app.post("/tasks")
def add_task():
    t = {"id": len(tasks)+1, "title": request.json["title"], "done": False}
    tasks.append(t); return jsonify(t), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
