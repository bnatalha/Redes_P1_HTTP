from flask import Flask, jsonify, abort
from flask_restful import Api, Resource, reqparse, request

app = Flask(__name__)
users = [
    {
        "nome": "Vao",
        "idade": "31",
        "altura": "1,61"
    },
    {
        "nome": "Tudo",
        "idade": "38",
        "altura": "1,71"
    },
    {
        "nome": "Reprovar",
        "idade": "26",
        "altura": "2,01"
    },
    {
        "nome": "kjkBrinks",
        "idade": "15",
        "altura": "1,56"
    }
]
#api = Api(app)
@app.route('/')
def index():
    return 'Hello World'

@app.route('/user/getuser/<string:nome>', methods=['GET'])
def getuser(nome):
    for user in users:
        if(nome == user["nome"]):
            return jsonify({'users': user})
    return "Usuario inexistente.", 404

@app.route('/user/getuser/lista', methods=['GET'])
def listUsers():
    return jsonify({'users': users}), 200

@app.route('/user/getuser/post', methods=['POST'])
def post():
    parser = reqparse.RequestParser()
    parser.add_argument("idade")
    parser.add_argument("altura")
    parser.add_argument("nome")
    args = parser.parse_args()
    nome = request.args.get('nome')
    print nome
    for user in users:
        if(args["nome"] == user["nome"]):
            return "Usuario ja {} existe!".format(args['nome']), 400 # bad request
    user = {
        "nome": args["nome"],
        "idade": args["idade"],
        "altura": args["altura"]
    }
    users.append(user)
    return jsonify({'user': user}), 201 #Criado com sucesso

@app.route('/user/getuser/put', methods=['PUT'])
def put():
    parser = reqparse.RequestParser()
    parser.add_argument("idade")
    parser.add_argument("altura")
    parser.add_argument("nome")
    args = parser.parse_args()
    nome = args["nome"]
    for user in users:
        if(nome == user["nome"]):
            user["idade"] = args["idade"]
            user["altura"] = args["altura"]
            return jsonify({'user': user}), 200 #Atualizado com sucesso
    return "Usuario inexistente. Nada a atualizar.", 404

@app.route('/user/getuser/del/<string:nome>', methods=['DELETE'])
def delete(nome):
    count = 0
    for user in users:
        if (user["nome"] == nome):
            users.pop(count)
            return "Usuario {} deletado com sucesso.\n".format(nome), 200
        else:
            count = count + 1
    return "Usuario inexistente. Nada a atualizar.\n", 404

#api.add_resource(User, "/user/<string:nome>")
app.run(host='0.0.0.0', port=9999,debug=True)
