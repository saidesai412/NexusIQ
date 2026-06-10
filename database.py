from motor.motor_asyncio import AsyncIOMotorClient
import redis.asyncio as aioredis
from loguru import logger
from app.config import settings

# MongoDB
mongo_client: AsyncIOMotorClient = None
mongo_db = None

# Redis
redis_client = None


async def init_db():
    global mongo_client, mongo_db, redis_client

    # MongoDB
    try:
        mongo_client = AsyncIOMotorClient(settings.MONGO_URI)
        await mongo_client.admin.command("ping")
        mongo_db = mongo_client.get_default_database()
        logger.info("MongoDB connected")
    except Exception as e:
        logger.error(f"MongoDB connection failed: {e}")

    # Redis
    try:
        redis_client = await aioredis.from_url(
            settings.REDIS_URL,
            encoding="utf-8",
            decode_responses=True,
        )
        await redis_client.ping()
        logger.info("Redis connected")
    except Exception as e:
        logger.warning(f"Redis connection failed (continuing without cache): {e}")


async def close_db():
    global mongo_client, redis_client

    if mongo_client:
        mongo_client.close()
        logger.info("MongoDB disconnected")

    if redis_client:
        await redis_client.close()
        logger.info("Redis disconnected")


def get_mongo_db():
    return mongo_db


async def get_redis():
    return redis_client


async def cache_set(key: str, value: str, ttl: int = 300):
    if redis_client:
        try:
            await redis_client.setex(key, ttl, value)
        except Exception as e:
            logger.warning(f"Cache set failed: {e}")


async def cache_get(key: str):
    if redis_client:
        try:
            return await redis_client.get(key)
        except Exception as e:
            logger.warning(f"Cache get failed: {e}")
    return None


async def cache_delete(key: str):
    if redis_client:
        try:
            await redis_client.delete(key)
        except Exception as e:
            logger.warning(f"Cache delete failed: {e}")
