import redis

#
# r = redis.Redis(host='192.168.2.104', port=6379, db=0)
# r.set('name', 'xinping')
#
# print(r.get("name"))


pool = redis.ConnectionPool(host='192.168.2.104', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
r.set('name', "redis_conn_pool")
print(r.get("name"))
