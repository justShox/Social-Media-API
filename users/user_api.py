from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette import status
from users import RegisterValidator, EditValidator
from database.userservice import (register_user_db, login_user_db, get_exact_user_db, get_all_users_db,
                                  delete_user_db, edit_user_info_db, upload_profile_photo_db, delete_profile_photo_db)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
# Создать компонент
user_router = APIRouter(prefix='/users', tags=['Управление с пользователями'])


# Запрос для регистрации
@user_router.post('/register')
async def register_user(data: RegisterValidator):
    result = register_user_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'Такой пользователь уже имеется'}


# Запрос для логина
@user_router.post('/login')
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = login_user_db(form_data.username, form_data.password)

    if not user:
        raise HTTPException(status_code=400, detail='Неверный номер или пароль')
    else:
        return user


# Запрос для получения всех пользователей
@user_router.get('/all-user')
async def get_all_users():
    return get_all_users_db()


# Запрос для получения определенного пользователя
@user_router.get('/user')
async def get_exact_user(user_id: int):
    return get_exact_user_db(user_id)


# Запрос для удаления пользователя
@user_router.delete('/delete-user')
async def delete_user(user_id: int):
    return delete_user_db(user_id)


# Запрос для изменения данных пользователя
@user_router.put('/edit-user')
async def edit_user(data: EditValidator):
    change_data = data.model_dump()
    edit = edit_user_info_db(**change_data)
    return edit


# # Запрос для загрузки фото профиля
# @user_router.post('/upload-photo')
# async def upload_photo(user_id: int):

# Запрос для удаления фото профиля
@user_router.post('/delete-photo')
async def delete_photo(user_id: int):
    return delete_profile_photo_db(user_id)
