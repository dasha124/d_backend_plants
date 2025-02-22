import psycopg2
import environ
env = environ.Env()

conn = psycopg2.connect(
    user=env('DATABASE_USER'),
    password=env('DATABASE_PASSWORD'),
    host=env('DATABASE_HOST'),
    port=env('DATABASE_PORT'),
    database=env('DATABASE_NAME'),
)

cursor = conn.cursor()

plant_subclass_data = [
        {
        # "plant_subclass_id": 2,
        "subclass_name": "Лампочки",
        "image_url_subclass": "null",
        "plant_class_id": 2
    },
    {
        # "plant_subclass_id": 1,
        "subclass_name": "Кактусы, суккуленты",
        "image_url_subclass": "null",
        "plant_class_id": 1
    },
    {
        # "plant_subclass_id": 6,
        "subclass_name": "Альпинисты",
        "image_url_subclass": "null",
        "plant_class_id": 2
    },
    {
        # "plant_subclass_id": 16,
        "subclass_name": "Декоративные травы",
        "image_url_subclass": "null",
        "plant_class_id": 2
    },
    {
        # "plant_subclass_id": 18,
        "subclass_name": "Папоротники",
        "image_url_subclass": "null",
        "plant_class_id": 2
    },
]

insert_query = """
    INSERT INTO "Plant_Subclass" (subclass_name, image_url_subclass, plant_class_id)
    VALUES (%s, %s, %s)
"""

insert_values = [(plant['subclass_name'], 
                  plant['image_url_subclass'], 
                  plant['plant_class_id']) for plant in plant_subclass_data]

cursor.executemany(insert_query, insert_values)
conn.commit()


cursor.close()
conn.close()

print(f"Добавлены классы растения в базу данных.")
