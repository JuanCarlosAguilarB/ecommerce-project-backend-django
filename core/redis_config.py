import redis
from django.conf import settings


class RedisSingleton:
    """
    A singleton class to manage a single Redis connection instance throughout the application.
    This class ensures that only one instance of the Redis connection is created and shared across the application.

    Usage:
        To retrieve the Redis connection instance, use the `get_instance` method:
        redis_instance = RedisSingleton.get_instance()

    Note:
        Ensure that Django settings (`REDIS_HOST`, `REDIS_PORT`, `REDIS_DB`) are properly configured
        before using this class to establish a connection to Redis.
    """

    _instance = None

    @staticmethod
    def get_instance():
        """
        Retrieve the Redis connection instance.
        If an instance doesn't exist, create a new connection to Redis using Django settings.

        :return: Singleton instance of the Redis connection.
        """
        if RedisSingleton._instance is None:
            url = f'redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}'
            RedisSingleton._instance = redis.StrictRedis.from_url(
                url=url
                # db=settings.REDIS_DB
                )
        return RedisSingleton._instance
