from pydantic import BaseModel


# Валидатор для публикации
class PublicPostValidator(BaseModel):
    user_id: int
    post_text: str


# Валидатор для изменения данных в посте
class EditPostValidator(BaseModel):
    post_id: int
    new_text: str
