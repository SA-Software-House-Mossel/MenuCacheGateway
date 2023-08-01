from rediscluster import RedisCluster
import json


def lambda_handler(event, context):
    redis = RedisCluster(
        startup_nodes=[{"host": "dev-product-cache.1izp2r.clustercfg.afs1.cache.amazonaws.com", "port": "6379"}],
        decode_responses=True, skip_full_coverage_check=True)

    pinged = 'Hi Redis'
    if not redis.ping():
        pinged = 'Not Redis'

    redis.set('foo', 'bar')
    value = redis.get('foo')
    value2 = json.dumps(redis.get('815744_EA'))

    return {
        'statusCode': 200,
        'body': value + " " + value2
    }
