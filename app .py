from flask import Flask, render_template
from cefpython3 import cefpython as cef

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    cef.Initialize()
    cef.CreateBrowserSync(url='http://localhost:5000', window_title='Maya:TS')
    cef.MessageLoop()
    cef.Shutdown()
