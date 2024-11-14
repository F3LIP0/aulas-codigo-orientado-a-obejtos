from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Lista de tarefas
tasks = [
    {"id": 1, "title": "Comprar leite", "done": False},
    {"id": 2, "title": "Estudar Python", "done": False}
]

#cachorro.com.br/tasks
# Endpoint para retornar todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/site', methods=['GET'])
def get_site():
    return "<p> isso é um site </p> <div style='background-color:#546ef0;width:100px;height:100px;'> &nbsp; <button onclick='window.location=`https://google.com`'>isso é um botao</button></div>"

# Endpoint para retornar uma tarefa específica
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({"error": "Tarefa não encontrada"}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        tasks.remove(task)
        return jsonify({"message": "Tarefa apagada com sucesso"}), 200
    return jsonify({"error": "Tarefa não encontrada"}), 404

# Endpoint para criar uma nova tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = request.json
    new_task["id"] = len(tasks) + 1
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Tarefa não encontrada"}), 404
    data = request.json
    task.update({
        "title": data.get("title", task["title"]),
        "done": data.get("done", task["done"])
    })
    
    return jsonify({"message": "Tarefa atualizada com sucesso", "task": task}), 200

# Rodar a aplicação
if __name__ == '__main__':
    app.run(debug=True)