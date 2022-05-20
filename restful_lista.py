from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

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

# Esta classe visualiza uma tarefa, muda o status de uma tarefa e deleta uma tarefa
class GerenciarTarefas(Resource):
    def get(self, id):
        return lista_de_tarefa[id]

    def put(self, id):
        dados = json.loads(request.data)
        lista_de_tarefa[id]["status"] = dados
        return {'status': 'sucesso', 'messagem': 'status atualizado'}

    def delete(self, id):
        lista_de_tarefa.pop(id)
        mensagem = f'A tarefa de id {id} foi deletada'
        for i in range(0, len(lista_de_tarefa)):
            lista_de_tarefa[i]["id"] = i
        return {'status': 'sucesso', 'messagem': mensagem}

# Esta classe adiciona um nova tarefa e visualiza a lista com todas as tarefas
class Tarefas(Resource):
    def get(self):
        return lista_de_tarefa

    def post(self):
        nova_tarefa = json.loads(request.data)
        nova_tarefa["id"] = len(lista_de_tarefa)
        lista_de_tarefa.append(nova_tarefa)
        mensagem = f'Tarefa adicionada no id {nova_tarefa["id"]}'
        return {'status': 'suceesso', 'messagem': mensagem}


api.add_resource(GerenciarTarefas, '/tarefa/<int:id>/')
api.add_resource(Tarefas, '/tarefa/')

if __name__ == '__main__':
    app.run(debug=True)