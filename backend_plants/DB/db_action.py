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

action_data = [
    {
        'action_name': 'Добавление',
    },
        {
        'action_name': 'Изменение',
    },
        {
        'action_name': 'Удаление',
    }

]

insert_query = """
    INSERT INTO "Action" (action_name)
    VALUES (%s)
"""
insert_values = [(action['action_name'],) for action in action_data]

cursor.executemany(insert_query, insert_values)

conn.commit()

cursor.close()
conn.close()

print(f"Добавлены действия в базу данных.")
