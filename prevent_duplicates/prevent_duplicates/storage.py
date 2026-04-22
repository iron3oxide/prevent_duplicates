import redis
import frappe


def get_redis_connection() -> redis.Connection:
    cache = frappe.cache
    assert cache is not None
    connection = cache.connection_pool.get_connection()
    assert connection is not None
    return connection