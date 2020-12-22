from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config


db=SQLAlchemy()
migrate = Migrate()
# create_app 함수 안에서 만든 객체는 지역 변수이므로...
# 다른 함수에서 쓸 수 있도록 따로 선언해서 만들어 준다

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    # ORM

    from . import models

    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    # blueprint로 main_views에서 가져옴
    app.register_blueprint(question_views.bp)
    # blueprint로 question_views에서 가져옴
    app.register_blueprint(answer_views.bp)

    # Filter datetime
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app

## 진도 나간 부분까지 https://wikidocs.net/81045