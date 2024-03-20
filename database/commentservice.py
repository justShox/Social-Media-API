from database.models import PostComment
from datetime import datetime
from database import get_db


# Опубликовать комментарий
def add_comment(post_id, user_id, comment_text):
    db = next(get_db())
    new_comment = PostComment(post_id=post_id,
                              user_id=user_id,
                              comment_text=comment_text,
                              publish_date=datetime.now())
    if new_comment:
        db.add(new_comment)
        db.commit()

        return 'Коммент добавлен'
    else:
        return 'Нету такого поста(('


# Удаления комментария
def delete_comment_db(post_id, comment_id):
    db = next(get_db())
    # Если не сработает, то здесь
    exact_comment = db.query(PostComment).filter_by(post_id=post_id, comment_id=comment_id).first()
    if exact_comment:
        db.delete(exact_comment)
        db.commit()
        return 'Успешно удалено'
    else:
        return 'Коммент не найден'


# Изменить определенный коммент
def change_comment_db(post_id, comment_id, change_text):
    db = next(get_db())
    exact_comment = db.query(PostComment).filter_by(post_id=post_id, comment_id=comment_id).first()
    if exact_comment:
        exact_comment.comment_text = change_text
        db.commit()
        return 'Коммент изменен'
    else:
        return 'Коммент не найден'


# Получить все коммент определенного поста
def get_post_comments_db(post_id):
    db = next(get_db())
    post_comments = db.query(PostComment).filter_by(post_id=post_id).all()
    if post_comments:
        return post_comments
    else:
        return 'Коммент не найден'
