from flask import Blueprint
from database.postservice import get_all_posts_db, get_exact_post_db, delete_exact_post_db, change_post_text_db, add_new_post_db
post_bp = Blueprint('user_post', __name__, url_prefix='/post')

#Получить все посты
@post_bp.route('/', methods=['GET'])
def get_all_user_posts():
    all_posts = get_all_posts_db()
    if all_posts:
        return  {'status': 1, 'message': all_posts}
    return {'status': 0, 'message': 'Not found'}

#Получить определенный пост
@post_bp.route('/<int:post_id>', methods = ['GET'])
def get_exact_post(post_id:int):
    exact_post = get_exact_post_db(post_id)
    if exact_post:
        return {'status': 1, 'message': exact_post}
    return {'status': 0, 'message': 'Not found'}

#Опубликовать пост
@post_bp.route('/upload_post', methods = ['POST'])
def create_post(post_text:str, post_photo:str, hashtags:list, user_id:int):
    # new_post = add_new_post_db(user_id=user_id, photo_id=post_photo, post_text=post_text)
    pass

#Изменить определенный пост
@post_bp.route('/<int:user_id>/<int:post_id>', methods = ['PUT'])
def change_user_post(user_id:int, post_id:int):
    #     return {'status': 1, 'message': 'Post changed'}
    # return {'status': 0, 'message': 'Not found'}
    pass

#Удалить определенный пост
@post_bp.route('/<int:user_id>/<int:post_id>', methods = ['DELETE'])
def delete_user_post(user_id:int, post_id:int):
    delete_user_post = delete_exact_post_db(user_id,post_id)
    if delete_user_post:
        return {'status': 1, 'message': 'Post deleted'}
    return {'status': 0, 'message': 'Not found'}