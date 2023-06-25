from flask import Blueprint, request

photo_bp = Blueprint('photo', __name__, url_prefix='/photo')

#Получить все фотографии всех пользователей
@photo_bp.route('/', methods=['GET'])
def get_all_photos():
    pass

#Публикация фотографии
@photo_bp.route('/', methods=['POST'])
def publish_photo():
    #Получить фото из фронт части
    file = request.files.get('image', '')
    file.save('user_images/'+file.filename)
    print (type(file))
    return 'hello'

#Получить фотографии определенного пользователя по user_id
@photo_bp.route('/<int:user_id>', methods = ['GET'])
def get_exact_user_photos(user_id:int):
    pass

#Получить определенную фотографию по photo_id
@photo_bp.route('/<int:photo_id>', methods = ['GET'])
def get_exact_photo(photo_id:int):
    pass

#Изменить определенную фотографию пользователя
@photo_bp.route('/<int:user_id>/<int:photo_id>', methods = ['PUT'])
def change_user_photo(user_id:int, photo_id:int):
    pass

#Удалить определенную фотографию пользователя
@photo_bp.route('/<int:user_id>/<int:photo_id>', methods = ['DELETE'])
def delete_user_photo(user_id:int, photo_id:int):
    pass
