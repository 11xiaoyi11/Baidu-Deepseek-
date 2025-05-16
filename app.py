from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from search import get_search_results
from chat_api import generate_answer, generate_prompt
import eventlet
import eventlet.wsgi
import os

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", ping_timeout=120, ping_interval=25)
current_dir = os.path.dirname(os.path.abspath(__file__))
prompt_path = os.path.join(current_dir, "prompts/prompt_no_history.txt")

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on('user_message')
def handle_message(data):
    user_msg = data['message']
    search_results = []
    # 获取搜索结果
    for result in get_search_results(user_msg):
        search_results.append(result)
        emit('search_result', result)
        eventlet.sleep(0.1)  # 非阻塞的异步睡眠，给前端留时间刷新

    # 搜索结束，通知前端
    emit('search_done')
    
    # 构建 Prompt 并调用模型
    prompt = generate_prompt(prompt_path, user_msg, search_results)
    answer = generate_answer(prompt)

    print("最终回答:", answer)
    emit('final_answer', {'answer': answer})

if __name__ == "__main__":
    socketio.run(app, debug=True)
