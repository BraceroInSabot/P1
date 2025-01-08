from .base import *
from dotenv import load_dotenv

load_dotenv(dotenv_path=".envs/django/.env")

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-#')

DEBUG = os.getenv('DEBUG', 'False')

ALLOWED_HOSTS = env['ALLOWED_HOSTS']
SITE_NAME = 'P1'