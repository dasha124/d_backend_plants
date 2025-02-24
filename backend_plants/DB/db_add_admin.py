import requests

REGISTER_URL = 'http://plantsbackend:8100/api/register_admin/'

users_data = [
    {
        "email": "admin_1@gmail.com",
        "username": "admin_1",
        "password": "admin_1"
    },
    {
        "email": "admin_2@gmail.com",
        "username": "admin_2",
        "password": "admin_2"
    }
]

for user_data in users_data:
    response = requests.post(REGISTER_URL, json=user_data)
    
    if response.status_code == 201:
        print(f"Админ успешно зарегистрирован.")
    else:
        print(f"Ошибка при регистрации {user_data['username']}: {response.json()}")

print("Процедура регистрации завершена.")
