from pydantic import BaseModel
from datetime import datetime


# Валидатор для публикации
class PublicPostValidator(BaseModel):
    user_id: int
    post_text: str


# Валидатор для изменения данных в посте
class EditPostValidator(BaseModel):
    post_id: int
    new_text: str
