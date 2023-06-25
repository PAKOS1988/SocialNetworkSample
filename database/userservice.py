from models import User, Password, db

#Регистрация
def register_user(**user_data):
    new_user = User(**user_data)
    db.session.add(new_user)
    db.session.commit()

#Проверка пользователя по почте
def check_user_db(email):
    pass

#Проверка пароля пользователя
def check_user_password_db(email, password):
    pass

#Получить всех пользователей из базы
def get_all_users_db():
    pass

#Получить определенного пользователя
def get_exact_user_db(user_id):
    pass

#Удалить пользователя из базы
def delete_user_db(user_id):
    pass