import requests

REGISTER_URL = 'http://plantsbackend:8100/api/register/'

users_data = [
    {
        "email": "user_1@gmail.com",
        "username": "user_1",
        "password": "user_1"
    },
    {
        "email": "user_2@gmail.com",
        "username": "user_2",
        "password": "user_2"
    }
]

for user_data in users_data:
    response = requests.post(REGISTER_URL, json=user_data)
    
    if response.status_code == 201:
        print(f"Пользователь успешно зарегистрирован.")
    else:
        print(f"Ошибка при регистрации {user_data['username']}: {response.json()}")

print("Процедура регистрации завершена.")
