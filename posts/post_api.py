from fastapi import APIRouter, UploadFile, Body
from database.postservice import *
from posts import PublicPostValidator, EditPostValidator

post_router = APIRouter(prefix='/posts', tags=['Для работы с публикациями'])


# Загружаем наши посты (Download)
@post_router.post('/publish')
async def publish_post(data: PublicPostValidator):
    result = add_new_post_db(**data.model_dump())
    if result:
        return {'message': result}
    else:
        return {'message': 'Пост не найден'}


# Запрос на удаление поста
@post_router.post('/delete-post')
async def delete_post(post_id: int):
    result = delete_post(post_id)
    if result:
        return {'message': result}
    else:
        return {'message': 'Пост не найден'}


# Запрос на получение всех постов
@post_router.get('/get-all-posts')
async def all_posts():
    result = get_all_posts_db()
    return result


# Запрос для добавления фото к посту
@post_router.post('/add-photo')
async def add_photo(post_id: int, photo_path: UploadFile = None):
    with open(f'media/{photo_path.filename}', mode='wb') as file:
        user_photo = await photo_path.read()
        file.write(user_photo)

    result = upload_post_photo_db(post_id, f'media/{photo_path.file}')

    if result:
        return {'message': result}
    else:
        return {'message': 'Что то пошло не так, попробуйте снова'}


# Изменить текст определенной публикации
@post_router.post('/edit-exact-post')
async def edit_exact_post(data: EditPostValidator):
    result = edit_post_text_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Что то пошло не так'}


# Запрос на получение определенного поста
@post_router.get('/post')
async def get_post(post_id):
    result = get_exact_post_db(post_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Что то пошло не так'}


# Запрос на получение всех фотографий
@post_router.get('/get-all-photos')
async def get_all_photos():
    result = all_photos_db()
    if result:
        return {'message': result}
    else:
        return {'message': 'Что то пошло не так'}


# Запрос на удаление фото определенного поста
@post_router.put('/delete-post-photo')
async def delete_post_photo(post_id: int):
    result = delete_post_photo_db(post_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Что то пошло не так'}


# Запрос на добавление лайка к посту
@post_router.put('/add-like')
async def add_like(post_id: int):
    result = like_post_db(post_id)
    if result:
        return {'message': result}
    else:
        return {'message': 'Что то пошло не так'}


# Запрос на удаление лайка к посту
@post_router.put('/delete-like')
async def delete_like(post_id: int):
    result = unlike_post_db(post_id)
    if result:
        return {'message': result}
    else:
        return {'message': 'Что то пошло не так'}
