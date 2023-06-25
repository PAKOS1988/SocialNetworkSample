from flask import Blueprint

comment_bp = Blueprint('comment', __name__, url_prefix='/comment')

#Получить комментарии определенного поста
@comment_bp.route('/<int:post_id>', methods=['GET'])
def get_exact_post_comments(post_id:int):
    pass

#Публикация комментария
@comment_bp.route('/<int:post_id>/<int:comment_user_id>', methods = ['POST'])
def publish_comment(post_id:int, comment_user_id:int):
    pass

#Изменить комментарий
@comment_bp.route('/<int:comment_user_id>/<int:comment_id>', methods = ['PUT'])
def change_comment(comment_user_id:int, comment_id:int):
    pass

#удалить комментарий
@comment_bp.route('/<int:comment_user_id>/<int:comment_id>', methods = ['DELETE'])
def delete_comment(comment_user_id:int, comment_id:int):
    pass
