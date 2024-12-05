from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    user_ip = request.remote_addr
    return f"<h1>Ваша IP-адреса: {user_ip}</h1>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
