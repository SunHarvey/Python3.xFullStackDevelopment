import redis

pool = redis.ConnectionPool(host='192.168.2.104', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
# r.set("name", "set_string", ex=30)
# print(r.get("name"))

# r.setnx('name2', 'xinping')
# print(r.get('name2'))

# r.setex("name3", "20", "xinping")
# print(r.get("name3"))

# r.mset(name5="wangwu", name6="liuliu")
r.mset({"name5": "wangwu", "name6": "liuliu"})

print(r.mget("name5", "name6"))
