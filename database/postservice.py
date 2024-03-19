from database.models import PostPhoto, UserPost
from database import get_db
from datetime import datetime


# Получить все публикации
def get_all_posts_db():
    db = next(get_db())
    all_post = db.query(UserPost).all()
    return all_post


# Получить определенную публикацию
def get_exact_post_db(post_id):
    db = next(get_db())
    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()
    if exact_post:
        return exact_post
    else:
        return 'Такой пост не обнаружен'


# Добавить публикации
def add_new_post_db(user_id, post_text):
    db = next(get_db())
    new_post = UserPost(user_id=user_id, post_text=post_text, publish_date=datetime.now())
    db.add(new_post)
    db.commit()
    return f'Успешно добавлен {new_post.post_id}'


# Изменить текст к публикации
def edit_post_text_db(post_id, new_text):
    db = next(get_db())
    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()

    if exact_post:
        exact_post.post_text = new_text
        db.commit()
        return 'Текст к публикации изменен!'
    else:
        return 'Пост не найден(('


# Удалить публикацию
def delete_post_db(post_id):
    db = next(get_db())
    delete_post = db.query(UserPost).filter_by(post_id=post_id).first()
    if delete_post:
        db.delete(delete_post)
        db.commit()
        return 'Пост удален!'
    else:
        return 'Пост не найден(('


# Добавить лайк к публикации
def like_post_db(post_id):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()

    if exact_post:
        exact_post.likes += 1
        db.commit()
        return '+1 like'
    else:
        return 'Пост не найден(('


# Удалить лайк из публикаций
def unlike_post_db(post_id):
    db = next(get_db())
    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()
    if exact_post:
        exact_post.likes -= 1
        db.commit()
        return '-1 like'
    else:
        return 'Пост не найден(('


# Загрузить фотографию к посту
def upload_post_photo_db(post_id, photo_path):
    db = next(get_db())

    new_photo = PostPhoto(post_id=post_id, photo_path=photo_path)

    if new_photo:
        db.add(new_photo)
        db.commit()
        return 'Фото добавлено!'
    else:
        return 'Пост не найден(('


# Удалить фотографию определенного поста
def delete_post_photo_db(post_id):
    db = next(get_db())
    del_photo = db.query(PostPhoto).filter_by(post_id=post_id).first()
    if del_photo:
        # Если не работает, то здесь
        del_photo.photo_path = None
        db.commit()
        return 'Фото удалено!'
    else:
        return 'Пост не найден(('


# Запрос на получение всех фотографий
def all_photos_db():
    db = next(get_db())
    photos = db.query(PostPhoto).all()
    return photos
