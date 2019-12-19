import redis

r = redis.StrictRedis(host='192.168.99.100', port=32768, charset="utf-8", decode_responses=True, db=0)

r.set('candidato1', 0)
r.set('candidato2', 0)

r.set('A', 'candidato1')
r.incr('candidato1')

r.set('B', 'candidato1')
r.incr('candidato1')

r.set('C', 'candidato2')
r.incr('candidato2')

r.set('D', 'candidato1')
r.incr('candidato1')

r.set('E', 'candidato2')
r.incr('candidato2')

# Consulta 

value = r.get('candidato1')
print(value)

value = r.get('candidato2')
print(value)


# Solução mais adequada para grande volume de dados, uma vez que não seria necessário percorrer todas as chaves do banco.
# Cada vez que um voto for computado, a chave referente ao valor do voto é incrementada. Assim, na consulta, basta verificar o valor de apenas duas chaves 
# (supondo a existência de apenas dois candidatos) 



