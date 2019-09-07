from redis import Redis

from sys import argv


config = {
   'host': '119.3.26.17',
   'port': argv[1],
   'db': 2
}

client = Redis(**config)

print('Redis 连接成功! %s' % str(config))