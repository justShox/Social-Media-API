from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from database import Base


# Таблица пользователя
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    surname = Column(String)
    phone_number = Column(String)
    city = Column(String)
    password = Column(String)
    birthday = Column(Date)
    profile_photo = Column(String)
    reg_date = Column(DateTime)


# Таблица публикаций
class UserPost(Base):
    __tablename__ = 'user_posts'
    post_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    post_text = Column(Text)
    likes = Column(Integer, default=0)
    publish_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')


# Таблица фотографий. Добавление фотографий к определенному посту
class PostPhoto(Base):
    __tablename__ = 'post_photo'
    photo_id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey('user_posts.post_id'))
    photo_path = Column(String)

    post_fk = relationship(UserPost, lazy='subquery')


# Таблица комментариев
class PostComment(Base):
    __tablename__ = 'post_comments'
    comment_id = Column(Integer, primary_key=True, autoincrement=True)

    user_id = Column(Integer, ForeignKey('users.user_id'))
    post_id = Column(Integer, ForeignKey('user_posts.post_id'))

    comment_text = Column(Text)
    publish_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')
    post_fk = relationship(UserPost, lazy='subquery')
