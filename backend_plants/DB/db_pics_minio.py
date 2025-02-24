import os
from minio import Minio
from minio.error import S3Error
import environ

env = environ.Env()
environ.Env.read_env()

def add_pic(pic_path: str):
    client = Minio(
        endpoint=env('AWS_S3_ENDPOINT_HOST'),
        access_key=env('AWS_ACCESS_KEY_ID'),
        secret_key=env('AWS_SECRET_ACCESS_KEY'),
        secure=env('AWS_USE_SSL', default=False)
    )
    
    i, _ = os.path.splitext(os.path.basename(pic_path))
    img_obj_name = f"{i}.png"
    print("Название растения:", i)

    if not os.path.exists(pic_path):
        return {"error": f"Файл не найден по указанному пути: {pic_path}"}
    
    bucket_name = 'logo'
    try:
        if not client.bucket_exists(bucket_name):
            client.make_bucket(bucket_name)
            print(f"Бакет '{bucket_name}' был успешно создан.")
        else:
            print(f"Бакет '{bucket_name}' уже существует.")
    except S3Error as e:
        print(f"Ошибка при создании бакета: {str(e)}")
    try:
        with open(pic_path, 'rb') as pic_file:
            client.put_object(
                bucket_name='logo',
                object_name=img_obj_name,
                data=pic_file,
                length=os.path.getsize(pic_path),
                content_type='image/png'
            )
        return {"message": "Успешно загружено!"}

    except S3Error as e:
        return {"error": f"S3 ошибка: {str(e)}"}
    except Exception as e:
        return {"error": f"Произошла ошибка: {str(e)}"}

response = add_pic('/app/media/images/Суккулент_1.jpeg')
print(response)
response = add_pic('/app/media/images/Суккулент_2.jpeg')
print(response) 
response = add_pic('/app/media/images/Суккулент_3.jpeg')
print(response)
response = add_pic('/app/media/images/Тюльпан_1.jpeg')
print(response) 
response = add_pic('/app/media/images/Тюльпан_2.jpeg')
print(response)
response = add_pic('/app/media/images/Тюльпан_3.jpeg')
print(response) 
response = add_pic('/app/media/images/Фонтанная трава "Рыжая Голова"_1.jpg')
print(response) 
response = add_pic('/app/media/images/Фонтанная трава "Рыжая Голова"_2.jpg')
print(response)
response = add_pic('/app/media/images/Фонтанная трава "Рыжая Голова"_3.jpg')
print(response) 



def add_pic_type(pic_path: str):
    client = Minio(
        endpoint=env('AWS_S3_ENDPOINT_HOST'),
        access_key=env('AWS_ACCESS_KEY_ID'),
        secret_key=env('AWS_SECRET_ACCESS_KEY'),
        secure=env('AWS_USE_SSL', default=False)
    )
    
    i, _ = os.path.splitext(os.path.basename(pic_path))
    img_obj_name = f"{i}.png"
    print("Название типа растения:", i)

    if not os.path.exists(pic_path):
        return {"error": f"Файл не найден по указанному пути: {pic_path}"}
    
    bucket_name = 'logo.type'
    try:
        if not client.bucket_exists(bucket_name):
            client.make_bucket(bucket_name)
            print(f"Бакет '{bucket_name}' был успешно создан.")
        else:
            print(f"Бакет '{bucket_name}' уже существует.")
    except S3Error as e:
        print(f"Ошибка при создании бакета: {str(e)}")
    try:
        with open(pic_path, 'rb') as pic_file:
            client.put_object(
                bucket_name='logo.type',
                object_name=img_obj_name,
                data=pic_file,
                length=os.path.getsize(pic_path),
                content_type='image/png'
            )
        return {"message": "Успешно загружено!"}

    except S3Error as e:
        return {"error": f"S3 ошибка: {str(e)}"}
    except Exception as e:
        return {"error": f"Произошла ошибка: {str(e)}"}

response = add_pic_type('/app/media/images/Суккулент_1.jpeg')
print(response)
response = add_pic_type('/app/media/images/Суккулент_2.jpeg')
print(response) 
response = add_pic_type('/app/media/images/Суккулент_3.jpeg')
print(response)
response = add_pic_type('/app/media/images/Тюльпан_1.jpeg')
print(response) 
response = add_pic_type('/app/media/images/Тюльпан_2.jpeg')
print(response)
response = add_pic_type('/app/media/images/Тюльпан_3.jpeg')
print(response) 
response = add_pic_type('/app/media/images/Фонтанная трава "Рыжая Голова"_1.jpg')
print(response) 
response = add_pic_type('/app/media/images/Фонтанная трава "Рыжая Голова"_2.jpg')
print(response)
response = add_pic_type('/app/media/images/Фонтанная трава "Рыжая Голова"_3.jpg')
print(response) 