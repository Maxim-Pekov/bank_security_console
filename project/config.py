from environs import Env


env = Env()
env.read_env()
DEBUG = env.bool('DEBUG')

DATABASES = {"default": env.dj_db_url("DATABASE_URL")}


