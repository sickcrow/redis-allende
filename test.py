import redis

try:
    conn = redis.StrictRedis(
        host='192.168.32.234',
        port=31666)
        #password='YOUR_PASSWORD')
    print (conn)
    conn.ping()
    print ('Connection OK')
except Exception as ex:
    print ('Error:'), ex
    exit('Failed to connect, terminating.')