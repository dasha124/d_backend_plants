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

plant_class_data = [
    {
        'class_name': 'Домашнее',
    },
    {
        'class_name': 'Садовое',
    }
]

insert_query = """
    INSERT INTO "Plant_Class" (class_name)
    VALUES (%s)
"""

insert_values = [(pl_class['class_name'],) for pl_class in plant_class_data]

cursor.executemany(insert_query, insert_values)
conn.commit()


cursor.close()
conn.close()

print(f"Добавлены классы растения в базу данных.")
