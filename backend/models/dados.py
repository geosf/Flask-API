from flask_restplus import fields

from backend.server.instance import server

post_dado = server.api.model('POST - Dados', {
    'A': fields.String(name='A',description="Lista de árvores com seu respectivo número de maçãs. Para inputar esses dados, necessário utilizar o padrão separado apenas por vírgula: 0,0,0,0 ... Quantas vezes quiser.",required=True),
    'K': fields.Integer(name='K',description="Número de árvores consecutivas que Marcelo irá colher maçãs.",required=True),
    'L':fields.Integer(name='L',description="Número de árvores consecutivas que Carla irá colher maçãs.",required=True)
})

get_dado = server.api.model('GET - Quantidade Máxima de Maçãs', {
    'qtd_macas': fields.Integer(name='qtd_macas',required=True, description='Quantidade máxima de maçãs coletadas por Marcelo e Carla.')
})