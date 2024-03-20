from pydantic import BaseModel


# Валидатор для добавления комментария
class PublishCommentValidator(BaseModel):
    post_id: int
    user_id: int
    comment_text: str


# Валидатор для изменения комментария
class EditCommentValidator(BaseModel):
    post_id: int
    comment_id: int
    change_text: str
