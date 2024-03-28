from database.security import create_access_token
from .models import User
from database import get_db


# Получить всех пользователей
def get_all_users_db():
    db = next(get_db())
    get_all_users = db.query(User).all()
    return get_all_users


# Получить определенного пользователя
def get_exact_user_db(user_id):
    db = next(get_db())
    checker = db.query(User).filter_by(user_id=user_id).first()
    if checker:
        return f'Пользователь найден {checker.user_id}'
    else:
        return 'Пользователь не обнаружен'


# Регистрация пользователя
def register_user_db(username, surname, phone_number, city, password):
    db = next(get_db())
    checker = db.query(User).filter_by(phone_number=phone_number).first()
    if checker:
        return 'Такой номер телефона уже есть в базу'
    else:
        new_user = User(username=username, surname=surname, phone_number=phone_number, city=city, password=password)
        db.add(new_user)
        db.commit()
        return f'Успешно зарегистрированы {new_user.user_id}'


# Логин пользователя
def login_user_db(username, password):
    db = next(get_db())
    checker = db.query(User).filter_by(username=username, password=password).first()
    if checker:
        token_data = {'user_id': checker.user_id}
        access_token_data = create_access_token(token_data)
        return {'access_token': access_token_data, 'token_time': 'Bearer', 'status': 'Success'}
    else:
        return f'Аккаунт с номером  не найден'


# Удаления пользователя
def delete_user_db(user_id):
    db = next(get_db())
    checker = db.query(User).filter_by(user_id=user_id).first()
    if checker:
        db.delete(checker.user_id)
        db.commit()
    else:
        return 'Пользователь не найден'


# Изменение данных пользователя
def edit_user_info_db(user_id, edit_info, new_info):
    db = next(get_db())
    exact_user = db.query(User).filter_by(user_id=user_id).first()
    if exact_user:
        if edit_info == 'username':
            exact_user.username = new_info
        elif edit_info == 'surname':
            exact_user.surname = new_info
        db.commit()
        return f'Данные успешно обновлены'
    else:
        return 'Пользователь не найден('


# Добавить фото профиля
def upload_profile_photo_db(user_id, photo_path):
    db = next(get_db())
    exact_user = get_exact_user_db(user_id=user_id)
    if exact_user:
        exact_user.profile_photo = photo_path
        db.commit()
        return 'Успешно!'
    else:
        return 'Пользователь не найден(('


# Удаления фото профиля
def delete_profile_photo_db(user_id):
    db = next(get_db())
    exact_user = get_exact_user_db(user_id)
    if exact_user:
        exact_user.profile_photo = 'None'
        db.commit()
        return 'Фото профиля удалено'
    else:
        return 'Пользователь не найден(('
