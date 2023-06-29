from database.models import Post, PostPhoto, PostComment, db

#Получить все посты
def get_all_posts_db():
    posts = Post.query.all()
    return posts

#Получить все изображения
def get_all_photos_db():
    photos = PostPhoto.query.all()
    return photos

#Получить все изображения определенного пользователя
def get_exact_user_photos_db(user_id):
    exact_user_photo = PostPhoto.query.filter_by(user_id=user_id).first()
    return exact_user_photo

#Получить определенную фоторгафию по photo_id
def get_exact_photo_db(photo_id):
    exact_photo = PostPhoto.query.filter_by(photo_id=photo_id).first()
    return exact_photo

#Изменить определенную фоторгафию пользователя по user_id и photo_id
def change_exact_user_photo_db(user_id, photo_id, photo_path):
    change_exact_user_photo = PostPhoto.query.filter_by(photo_id=photo_id, user_id=user_id).first()
    if change_exact_user_photo:
        change_exact_user_photo.photo_path = photo_path
        db.session.commit()


#Получить определенный пост
def get_exact_post_db(post_id):
    exact_post = Post.query.filter_by(post_id=post_id).first()
    return exact_post

#Удалить определенный пост
def delete_exact_post_db(post_id):
    delete_post = Post.query.filter_by(post_id=post_id).first()
    if delete_post:
        db.session.delete(delete_post)
        db.session.commit()
    else:
        return False

#Изменить текст поста
def change_post_text_db(post_id, new_text):
    post = Post.query.filter_by(post_id=post_id).first()
    if post:

        post.post_text = new_text
        db.session.commit()

#Добавить комментарий к посту
def add_comment_post_db(post_id, comment_user_id, comment_text):
    post = Post.query.filter_by(post_id=post_id).first()
    if post:
        new_comment = PostComment(post_id=post_id, user_id=comment_user_id, comment_text=comment_text)
        db.session.add(new_comment)
        db.session.commit()