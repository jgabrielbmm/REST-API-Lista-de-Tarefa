from flask import Flask, jsonify, request
import json

app = Flask(__name__)

lista_de_tarefa = [

    {
        'id':0,
        'responsável':'Gabriel',
        'tarefa':'Fazer uma REST API',
        'status':'pendente'
    },

    {
        "id": 1,
        "responsável": "Lucas",
        "tarefa": "Estudar Flask",
        "status": "concluida"
    }

]

@app.route('/tarefa/<int:id>', methods=['GET'])
# mostrar apenas uma tarefa
def visualisar_uma_tarefa(id):
    if request.method == 'GET':
        return jsonify(lista_de_tarefa[id])
# deletar uma tarefa
@app.route('/tarefa/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    if request.method == 'DELETE':
        lista_de_tarefa.pop(id)
        mensagem = f'A tarefa de id {id} foi deletada'
        for i in range(0, len(lista_de_tarefa)):
            lista_de_tarefa[i]["id"] = i
        return jsonify({'status': 'sucesso', 'messagem': mensagem})

# atualizar uma tarefa (obs: pode-se mudar apenas o status da tarefa)
@app.route('/tarefa/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    if request.method == 'PUT':
        dados = json.loads(request.data)
        lista_de_tarefa[id]["status"] = dados
        return jsonify({'status': 'sucesso', 'messagem': 'status atualizado'})


# mostrar todas as tarefas cadastradas
@app.route('/tarefa/', methods=['GET'])
def mostrar_todas_tarefas():
    if request.method == 'GET':
        return jsonify(lista_de_tarefa)

# adicionar uma nova tarefa
@app.route('/tarefa/', methods=['POST'])
def adicionar_tarefa():
    if request.method == 'POST':
        nova_tarefa = json.loads(request.data)
        nova_tarefa["id"] = len(lista_de_tarefa)
        lista_de_tarefa.append(nova_tarefa)
        mensagem = f'Tarefa adicionada no id {nova_tarefa["id"]}'
        return jsonify({'status':'suceesso', 'messagem':mensagem})



if __name__ == '__main__':
    app.run()
