from flask import Flask, render_template
import webview

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    window = webview.create_window('Maya:TS', 'http://localhost:2000')
    webview.start()
