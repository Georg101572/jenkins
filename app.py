from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    student_name = os.environ.get('STUDENT_NAME', 'Student-yashking')
    return f'Hello, {student_name}!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8099))
    app.run(host='158.160.194.244', port=port)
