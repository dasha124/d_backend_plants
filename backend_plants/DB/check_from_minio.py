import requests
import environ
env = environ.Env()

HOST_BACKEND = env('HOST_BACKEND')
PORT=env('PORT')
REGISTER_URL = f'http://{HOST_BACKEND}:{PORT}/api/from_minio/'

print("Процедура приверки минио завершена.")
