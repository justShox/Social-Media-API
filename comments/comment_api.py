from fastapi import APIRouter
from database.commentservice import *
from comments import PublishCommentValidator, EditCommentValidator

comment_router = APIRouter(prefix='/comments', tags=['Для работы с комментариями'])


# Опубликовать комментарий
@comment_router.post('/publish-comment')
async def publish_comment(data: PublishCommentValidator):
    result = add_comment(**data.model_dump())
    if result:
        return 'Комментарий опубликован'
    else:
        return 'Что то пошло не так'


# Изменить комментарий
@comment_router.put('/edit-comment')
async def edit_comment(data: EditCommentValidator):
    result = change_comment_db(**data.model_dump())
    if result:
        return 'Коммент изменен'
    else:
        return 'Что то пошло не так'


# Получить все комментарии определенного поста
@comment_router.get('/get-all-comments')
async def get_all_comments(post_id: int):
    result = get_post_comments_db(post_id)
    return result


# Удалить определенный коммент
@comment_router.put('/delete-comment')
async def delete_comment(post_id: int, comment_id: int):
    result = delete_comment_db(post_id, comment_id)
    return result
