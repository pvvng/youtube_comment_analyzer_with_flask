# app/__init__.py
from flask import Flask
from flask_cors import CORS

def create_app():
    # Flask 애플리케이션 초기화
    app = Flask(__name__)
    # 모든 도메인에서의 요청 허용
    CORS(app)

    # 최대 요청 본문 크기 설정 (예: 10MB)
    app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB

    # 블루프린트 등록
    from app.routes.sentiment import sentiment_bp 
    app.register_blueprint(sentiment_bp, url_prefix='/api')  # '/api' 프리픽스 추가

    return app
