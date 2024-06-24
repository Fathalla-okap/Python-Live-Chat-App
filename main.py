from flask import Flask, render_template, session
from flask_socketio import send, emit, SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = "hjhjsdahhds"
socketio = SocketIO(app)

messages = []

@app.route("/", methods=["GET"])
def home():
    session.clear()
    session["name"] = "unknown"
    return render_template("room.html", messages=messages)

@socketio.on("message")
def message(data):
    content = {
        "name": session.get("name"),
        "message": data["data"]
    }
    messages.append(content)
    send(content, broadcast=True)
    print(f"{session.get('name')} said: {data['data']}")

if __name__ == "__main__":
    socketio.run(app, debug=True)
