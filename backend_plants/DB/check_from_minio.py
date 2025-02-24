import requests
import environ
env = environ.Env()

HOST_BACKEND = env('HOST_BACKEND')
REGISTER_URL = f'http://{HOST_BACKEND}:8100/api/from_minio/'

print("Процедура приверки минио завершена.")
