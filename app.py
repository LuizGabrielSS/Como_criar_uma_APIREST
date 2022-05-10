#Importando o arquivo com os bancos e tabelas
from BD import *

#Importando biblioteca necessaria para deixar as suas respostas em formato json
import json
'''
Bibliotecas utilizadas no Flask para a criação de rota, entre elas pode encontrar as necessarias para
a criação de rotas seguras, pode encontrar p=por mais sobre a criação de uma rota segura no repositorio 
API-SEGURA
'''
from flask_jwt_extended import jwt_required, create_access_token,get_jwt_identity,JWTManager
from flask import Flask,request,jsonify,json

#Biblioteca necessaria para poder solicitar o que for necessario como variaveis especificas que serão usadas nas rotas
import requests

#Biblioteca necessaria caso a API e o que a estiver consumindo estiverem na mesma maquina
from flask_cors import CORS

app = Flask('APP')

CORS(app)

app.config["JWT_SECRET_KEY"] = 'Utilize uma senha boa e confiavel, de preferencia criptografada e hash'

jwt = JWTManager(app)

#Essa rota pode er testada com o uso do seu navegador padrão
@app.route('/teste-get', methods=['GET'])
def nao_segura():
    return "Dessa forma não será tao seguro, mas pode ser utilizado se essa rota não for necessariamente perigosa ou sigilosa"

#Essa rota só pode ser testada com o seu programa de teste de Api
#Sugiro o uso do postman, pode ser complexo no começo, mas ele compensa
@app.route('/teste-post', methods=['POST'])
def mais_segura():
    return "Dessa forma suas requisições ficam um pouco mais seguras"

#Aqui você vai testar recuperar os dados enviados por quem fez a requisição
@app.route('/teste-recuperando', methods=['POST'])
def recuperar():
    dados = request.get_json()
    return "você enviou"+dados

if __name__ == '__main__':
    host="Servidor da api, ou seja, o IP da maquina onde ela esta rodando"
    port="porta onde deseja rodar a API, caso não passe nenhum valor, ela ira rodar na porta 5000"
    app.run(host,port,debug=True)