import redis

r = redis.StrictRedis(host='localhost', port=6379, charset="utf-8", decode_responses=True, db=0)

r.set('A', 'candidato1')
r.set('B', 'candidato1')
r.set('C', 'candidato2')
r.set('D', 'candidato1')
r.set('E', 'candidato2')
r.set('F', 'candidato2')
r.set('G', 'candidato1')
r.set('H', 'candidato1')
r.set('I', 'candidato1')

allkeys = r.keys('*')
candidato1 = 0
candidato2 = 0
#1
for k in allkeys:    
    if r.get(k) == 'candidato1':
        candidato1 += 1
    else:
        candidato2 += 1

if candidato1 > candidato2:
    print('O Candidato 1 Venceu!')
else:
    print('O Candidato 2 Venceu!')

#2
votos = []
for k in allkeys:    
    votos.append(r.get(k))

candidato1 = votos.count('candidato1')
candidato2 = votos.count('candidato2')

if candidato1 > candidato2:
    print('O Candidato 1 Venceu!')
else:
    print('O Candidato 2 Venceu!')
