from flask import Flask, render_template
import webview
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def start_flask():
    app.run(host='127.0.0.1', port=5000)

if __name__ == '__main__':
    t = threading.Thread(target=start_flask)
    t.start()

    window = webview.create_window('Maya:TS', 'http://localhost:5000',width=640,height=360,frameless=True,transparent=True)
    webview.start()
