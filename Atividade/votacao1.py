import redis

r = redis.StrictRedis(host='192.168.99.100', port=32768, charset="utf-8", decode_responses=True, db=0)

allkeys = r.keys('*') 

candidato1, candidato2 = 0, 0

for c in allkeys:
    voto = r.get(c)
    if voto == 'candidato1' : 
        candidato1 += 1        
    elif voto == 'candidato2':
        candidato2 += 1
        
print(candidato1)      
print(candidato2)

if candidato1 > candidato2 : 
    print('Candidato 1 vencedor')
elif candidato2 > candidato1 :
    print('Candidato 2 vencedor')    
else : 
    print ("Empate")

print(allkeys)

#Solução não é adequada para grande volume de dados, uma vez que seria necessário percorrer todas as chaves do banco.


