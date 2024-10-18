# app/__init__.py
from flask import Flask
from flask_cors import CORS

def create_app():
    # Flask 애플리케이션 초기화
    app = Flask(__name__)
    # 모든 도메인에서의 요청 허용
    CORS(app)

    # 블루프린트 등록
    from app.routes.sentiment import sentiment_bp 
    app.register_blueprint(sentiment_bp, url_prefix='/api')  # '/api' 프리픽스 추가

    return app
