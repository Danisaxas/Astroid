import sys
from decouple import config
from dotenv import load_dotenv

# Cargar variables desde .env (para las demás configuraciones)
load_dotenv()

class Var:
    # API_ID FIJO
    API_ID = 27533879

    # Cargar API_HASH desde .env o usar el valor por defecto
    API_HASH = config("API_HASH", default="eb06d4abfb49dc3eeb1aeb98ae0f581e")
    SESSION = config("SESSION", default=None)
    REDIS_URI = config("REDIS_URI", default=None) or config("REDIS_URL", default=None)
    REDIS_PASSWORD = config("REDIS_PASSWORD", default=None)

    # Extras
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    LOG_CHANNEL = config("LOG_CHANNEL", default=0, cast=int)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
    HEROKU_API = config("HEROKU_API", default=None)
    VC_SESSION = config("VC_SESSION", default=None)
    ADDONS = config("ADDONS", default=False, cast=bool)
    VCBOT = config("VCBOT", default=False, cast=bool)

    # Railway
    REDISPASSWORD = config("REDISPASSWORD", default=None)
    REDISHOST = config("REDISHOST", default=None)
    REDISPORT = config("REDISPORT", default=None)
    REDISUSER = config("REDISUSER", default=None)

    # SQL y MongoDB
    DATABASE_URL = config("DATABASE_URL", default=None)
    MONGO_URI = config("MONGO_URI", default=None)