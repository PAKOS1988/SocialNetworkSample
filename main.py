from flask import Flask, render_template
from comment.comment_api import comment_bp
from hashtag.hashtag_api import hashtag_bp
from photo.photo_api import photo_bp
from posts.post_api import post_bp
from user.user_api import user_bp
from posts.post_api import post_bp
from flask_restx import Api
from database.models import db
from swagger.test_swagger import swagger_bp
api=Api()

app = Flask(__name__)
#Настройки базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///media.db'
db.init_app(app)
# Регистрация сайта к swagger
api.init_app(app)
@app.route('/')
def test_api():
    html_dexkan ='<h1>Test my api</h1><br><input type="file">'
    return render_template('test.html')
#Регистрация компонентов
app.register_blueprint(comment_bp)
app.register_blueprint(hashtag_bp)
app.register_blueprint(photo_bp)
app.register_blueprint(post_bp)
app.register_blueprint(user_bp)
#swagger
app.register_blueprint(swagger_bp)

#Запуск
# app.run()