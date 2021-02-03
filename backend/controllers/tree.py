from flask import Flask, json, request, jsonify
from flask_restplus import Api, Resource
from flask_cors import CORS

from backend.server.instance import server
from backend.models.dados import post_dado, get_dado

app, api = server.app, server.api
CORS(app)

db = []

def get_max_apples(A, K, L):
    total_macas = 0
    K = int(K)
    L = int(L)
    test = K + L

    if test>=int(len(A)):
        total_macas = -1
    else:
        for i in range(K):
            total_macas += int(A[i])
   
        for x in range(L):
            variavel = K + 1 + x
            total_macas += int(A[variavel])

    return total_macas

@api.route('/tree', methods=['GET', 'POST'])
class GetOrPost(Resource):
    #GET
    @api.marshal_with(get_dado)
    def get(self,):
        if not db:
            data = {'qtd_macas':"0"}
        else:
            A = db[0]['A'].split(",")
            K = db[0]['K']
            L = db[0]['L']
            data = { 'qtd_macas': get_max_apples(A, K, L) }     
        return data, 200
    #POST
    @api.expect(post_dado)
    @api.marshal_with(post_dado)
    def post(self,):
        if len(db) >= 1:
            db.clear()
        req = request.get_json()
        db.append(req)

        return db, 201
