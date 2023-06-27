from database.models import Post, PostPhoto, PostComment, db

#Получить все посты
def get_all_posts_db():
    posts = Post.query.all()
    return posts

#Получить все изображения
def get_all_photos_db():
    photos = PostPhoto.query.all()
    return photos

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