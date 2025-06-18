from flask import Flask, render_template
from flask_socketio import SocketIO, send
from translate import translate

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(msg):
    original = msg['text']
    translated = translate(original)
    out = {
        'user': msg['user'],
        'original': original,
        'translated': translated,
        'lang': msg['lang']
    }
    send(out, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)