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

# Примеры данных для вставки растений
plant_type_data = [
    {
        "type_name": "Суккулент",
        "plant_subclass_id": 1
    },

    {
        "type_name": "Тюльпан",
        "plant_subclass_id": 2
    },
    {
        "type_name": "Гиацинт",
        "plant_subclass_id": 2
    },
    {
        "type_name": "Фонтанная трава",
        "plant_subclass_id": 4
    },
    {
        "type_name": "Папоротник",
        "plant_subclass_id": 5
    },
]

insert_query = """
    INSERT INTO "Plant_Type" (type_name, plant_subclass_id)
    VALUES (%s, %s)
"""

insert_values = [(pl_type['type_name'], 
                  pl_type['plant_subclass_id']) for pl_type in plant_type_data]

cursor.executemany(insert_query, insert_values)

conn.commit()

cursor.close()
conn.close()

print(f"Добавлены виды растений в базу данных.")
