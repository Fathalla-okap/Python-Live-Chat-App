from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from flask_socketio import join_room, leave_room, send, SocketIO
import random
from string import ascii_uppercase

app = Flask(__name__)
app.config["SECRET_KEY"] = "hjhjsdahhds"
socketio = SocketIO(app)

messages = []

@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("room.html", messages=messages)

@socketio.on("message")
def message(data):
    content = {
        "name": session.get("name", "unknown"),
        "message": data["data"]
    }
    messages.append(content)
    send(content, broadcast=True)
    print(f"{content['name']} said: {content['message']}")

if __name__ == "__main__":
    socketio.run(app, debug=True)
