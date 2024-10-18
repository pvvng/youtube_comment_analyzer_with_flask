# application.py
from app import create_app

# Flask 애플리케이션 생성
app = create_app()

@app.route('/')
def say_hello():
    return "Hello Flask", 200

if __name__ == '__main__':
    app.run(debug=True)

# 가상환경 키는법
# .\venv\Scripts\activate
# 디버깅 키는 법
# flask --debug run