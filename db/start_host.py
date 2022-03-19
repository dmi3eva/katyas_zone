from flask import Flask, jsonify, request

# Settings for test
HOST = "0.0.0.0"
PORT = "5433"
DB_NAME = "katya_db"
USER = "katya"
PASSWORD = "100542"

app = Flask(__name__)

@app.route("/")
def usual():
    return "<p>Hello!</p>"


if __name__ == '__main__':
      app.run(host=HOST, port=PORT)