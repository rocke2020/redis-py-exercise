import redis
import os


class RedisUtil:
    def __init__(self, ip, port, password, db):
        self.__ip = ip
        self.__port = port
        self.__password = password
        self.__pool = redis.ConnectionPool(
            host=self.__ip,
            port=self.__port,
            password=self.__password,
            db=db,
            decode_responses=True,
            health_check_interval=10,
            socket_timeout=5,  # 连接超时时间（秒）
            socket_connect_timeout=5,  # 建立连接超时时间（秒）
            retry_on_timeout=True,
        )
        self.redis = redis.Redis(
            connection_pool=self.__pool, db=db, password=self.__password
        )

    def set(self, key, value, ex=None):
        """
        Set the value at key `name` to `value`

        :param key: Key to set
        :param value: Value to set
        :param ex: Expiration time in seconds
        :return: True if successful, False otherwise
        """
        return self.redis.set(key, value, ex=ex)

    def get(self, key):
        """
        Get the value of key `name`

        :param key: Key to get
        :return: Value of the key, or None if the key does not exist
        """
        return self.redis.get(key)

    def delete(self, key):
        """
        Delete one or more keys specified by `names`

        :param key: Key to delete
        :return: The number of keys that were removed
        """
        return self.redis.delete(key)

    def exists(self, key):
        """
        Check if a key exists

        :param key: Key to check
        :return: True if the key exists, False otherwise
        """
        return self.redis.exists(key)

    def expire(self, key, time):
        """
        Set a key's time to live in seconds

        :param key: Key to set expiration
        :param time: Time to live in seconds
        :return: True if successful, False otherwise
        """
        return self.redis.expire(key, time)

    def ttl(self, key):
        """
        Get the time to live for a key

        :param key: Key to get TTL
        :return: TTL in seconds, or -1 if the key does not have an expiration
        """
        return self.redis.ttl(key)

    def hset(self, name, key, value):
        """
        Set the value of a hash field

        :param name: Hash name
        :param key: Field name
        :param value: Field value
        :return: True if field is a new field in the hash and value was set, False if field already exists and the value was updated
        """
        return self.redis.hset(name, key, value)

    def hget(self, name, key):
        """
        Get the value of a hash field

        :param name: Hash name
        :param key: Field name
        :return: Value of the field, or None if the field does not exist
        """
        return self.redis.hget(name, key)

    def hdel(self, name, *keys):
        """
        Delete one or more hash fields

        :param name: Hash name
        :param keys: Field names to delete
        :return: The number of fields that were removed from the hash
        """
        return self.redis.hdel(name, *keys)

    def hgetall(self, name):
        """
        Get all the fields and values in a hash

        :param name: Hash name
        :return: Dictionary of field-value pairs
        """
        return self.redis.hgetall(name)

    def lpush(self, key, *values):
        """
        Prepend one or more values to the list stored at key `key`

        :param key: Key where the list is stored
        :param values: Values to prepend
        :return: The length of the list after pushing the new elements
        """
        return self.redis.lpush(key, *values)

    def rpush(self, key, *values):
        """
        Append one or more values to the list stored at key `key`

        :param key: Key where the list is stored
        :param values: Values to append
        :return: The length of the list after pushing the new elements
        """
        return self.redis.rpush(key, *values)

    def lrange(self, key, start, end):
        """
        Get a range of elements from the list stored at key `key`

        :param key: Key where the list is stored
        :param start: Start index
        :param end: End index
        :return: List of values in the specified range
        """
        return self.redis.lrange(key, start, end)

    def llen(self, key):
        """
        Get the length of the list stored at key `key`

        :param key: Key where the list is stored
        :return: Length of the list
        """
        return self.redis.llen(key)

    def lpop(self, key):
        """
        Remove and get the first element in the list stored at key `key`

        :param key: Key where the list is stored
        :return: The removed value, or None when key does not exist
        """
        return self.redis.lpop(key)

    def rpop(self, key):
        """
        Remove and get the last element in the list stored at key `key`

        :param key: Key where the list is stored
        :return: The removed value, or None when key does not exist
        """
        return self.redis.rpop(key)


if __name__ == "__main__":
    REDIS_DB = 0
    res = RedisUtil(
        ip=os.environ.get("REDIS_HOST_GPU", "localhost"),
        port=os.environ.get("REDIS_PORT_GPU", "6379"),
        password=os.environ.get("REDIS_PASSWORD_GPU", "foobared"),
        db=REDIS_DB,
    )
    print(res.redis.ping())
    print(res.redis.get("bike:1"))
    print(res.redis.get("bike:11"))
