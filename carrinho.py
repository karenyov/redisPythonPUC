import redis

r = redis.StrictRedis(host='localhost', port=6379, charset="utf-8", decode_responses=True, db=0)

a = [0, 1, 1, 2, 3, 5, 8, 13]
b = [0, 1, 1, 2, 3]

r.set('X', str(a))
r.set('Y', str(b))

value = r.get('X')
print(value)