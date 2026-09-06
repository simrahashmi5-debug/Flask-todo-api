from flask import Flask, request, jsonify
app = Flask(__name__)
todos = []
next_id = 1
@app.route('/')
def home():
    return "To-Do API is Running! Use /todos"
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)
@app.route('/todos', methods=['POST'])
def add_todo():
    global next_id
    data = request.get_json()
    new_task = {"id": next_id, "task": data.get("task"), "done": False}
    todos.append(new_task)
    next_id += 1
    return jsonify({"message": "Task added", "data": new_task}), 201
@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    global todos
    todos = [t for t in todos if t["id"] != id]
    return jsonify({"message": "Task deleted"})
if __name__ == '__main__':
    app.run(debug=True)
