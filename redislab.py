import redis

#conexão
r = redis.StrictRedis(host='localhost', port=6379, charset="utf-8", decode_responses=True, db=0)

#inserindo dados
r.set('A', 'candidato1')
r.set('B', 'candidato2')
r.set('C', 'candidato2')
r.set('D', 'candidato1')
r.set('E', 'candidato2')
r.set('F', 'candidato2')
r.set('G', 'candidato1')
r.set('H', 'candidato1')
r.set('I', 'candidato1')


