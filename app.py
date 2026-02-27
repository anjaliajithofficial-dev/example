from flask import Flask
from gpiozero import LED

app = Flask(__name__)
led = LED(17)

@app.route("/")
def home():
    return '''
    <h1>LED Control</h1>
    <a href="/on"><button>ON</button></a>
    <a href="/off"><button>OFF</button></a>
    '''

@app.route("/on")
def on():
    led.on()
    return '<h1>LED ON</h1><a href="/">Back</a>'

@app.route("/off")
def off():
    led.off()
    return '<h1>LED OFF</h1><a href="/">Back</a>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
