import psycopg2
import environ
env = environ.Env()

AWS_S3_ENDPOINT_URL = env('AWS_S3_ENDPOINT_URL')
conn = psycopg2.connect(
    user=env('DATABASE_USER'),
    password=env('DATABASE_PASSWORD'),
    host=env('DATABASE_HOST'),
    port=env('DATABASE_PORT'),
    database=env('DATABASE_NAME'),
)


cursor = conn.cursor()

# Примеры данных для вставки растений
plant_type_data = [
    {
        "type_name": "Суккулент",
        "plant_subclass_id": 1,
        "image_url_type": f'http://{AWS_S3_ENDPOINT_URL}/logo.type/Суккулент_3.png',
    },

    {
        "type_name": "Тюльпан",
        "plant_subclass_id": 2,
        "image_url_type": f'http://{AWS_S3_ENDPOINT_URL}/logo.type/Тюльпан_1.png',
    },
    {
        "type_name": "Гиацинт",
        "plant_subclass_id": 2,
        "image_url_type": f'http://{AWS_S3_ENDPOINT_URL}/logo.type/Тюльпан_1.png',
    },
    {
        "type_name": "Фонтанная трава",
        "plant_subclass_id": 4,
        "image_url_type": f'http://{AWS_S3_ENDPOINT_URL}/logo.type/Фонтанная трава "Рыжая Голова"_1.png',
    },
    {
        "type_name": "Папоротник",
        "plant_subclass_id": 5,
        "image_url_type": f'http://{AWS_S3_ENDPOINT_URL}/logo.type/Тюльпан_1.png',

    },
]

insert_query = """
    INSERT INTO "Plant_Type" (type_name, plant_subclass_id, image_url_type)
    VALUES (%s, %s, %s)
"""

insert_values = [(pl_type['type_name'], 
                  pl_type['plant_subclass_id'],
                  pl_type['image_url_type']) for pl_type in plant_type_data]

cursor.executemany(insert_query, insert_values)

conn.commit()

cursor.close()
conn.close()

print(f"Добавлены виды растений в базу данных.")
