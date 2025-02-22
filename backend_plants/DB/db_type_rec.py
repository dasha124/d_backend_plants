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

type_rec_data = [
    {
        'type_rec_name': 'по растению',
    },
    {
        'type_rec_name': 'по коллекции',
    }
]

insert_query = """
    INSERT INTO "Type_Recommendation" (type_rec_name)
    VALUES (%s)
"""

insert_values = [(type_rec['type_rec_name'],) for type_rec in type_rec_data]

cursor.executemany(insert_query, insert_values)
conn.commit()


cursor.close()
conn.close()

print(f"Добавлены типы рекомендаций в базу данных.")
