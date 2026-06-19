from flask import Flask, render_template, request
from config.db import DatabaseConfig
from config.extension import mysql
from routes.room_routes import room_bp
from routes.board_routes import board_bp
from flask_socketio import SocketIO, join_room, emit

app = Flask(__name__)

socketio = SocketIO(
    app,
    cors_allowed_origins="*"
)

# =========================
# ONLINE USERS MEMORY
# =========================

room_users = {}

user_sessions = {}

# =========================
# DATABASE CONFIG
# =========================

app.config["MYSQL_HOST"] = DatabaseConfig.HOST
app.config["MYSQL_USER"] = DatabaseConfig.USER
app.config["MYSQL_PASSWORD"] = DatabaseConfig.PASSWORD
app.config["MYSQL_DB"] = DatabaseConfig.DATABASE

mysql.init_app(app)

# =========================
# BLUEPRINTS
# =========================

app.register_blueprint(room_bp, url_prefix="/api")
app.register_blueprint(board_bp, url_prefix="/api")

# =========================
# ROUTES
# =========================

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/room/<int:room_id>")
def room(room_id):
    return render_template(
        "room.html",
        room_id=room_id
    )

# =========================
# SOCKET EVENTS
# =========================

@socketio.on("join_room")
def handle_join(data):

    room_id = str(data["room_id"])
    username = data["username"]

    join_room(room_id)

    # create room entry if not exists
    if room_id not in room_users:
        room_users[room_id] = []

    # prevent duplicate names
    if username not in room_users[room_id]:
        room_users[room_id].append(username)

    # store socket session
    user_sessions[request.sid] = {
        "room_id": room_id,
        "username": username
    }

    print("================================")
    print("USER JOINED")
    print("Room:", room_id)
    print("Username:", username)
    print("Current Users:", room_users)
    print("================================")

    # send updated user list
    emit(
        "room_users",
        room_users[room_id],
        room=room_id
    )

    # notify room
    emit(
        "user_joined",
        {
            "username": username
        },
        room=room_id
    )


@socketio.on("draw_end")
def handle_draw(data):

    room_id = str(data["room_id"])

    emit(
        "draw_end",
        data,
        room=room_id
    )


@socketio.on("clear_board")
def handle_clear(data):

    room_id = str(data["room_id"])

    emit(
        "clear_board",
        {},
        room=room_id
    )


@socketio.on("disconnect")
def handle_disconnect():

    sid = request.sid

    if sid not in user_sessions:
        return

    user = user_sessions[sid]

    room_id = user["room_id"]
    username = user["username"]

    if room_id in room_users:

        if username in room_users[room_id]:
            room_users[room_id].remove(username)

        # optional cleanup
        if len(room_users[room_id]) == 0:
            del room_users[room_id]

    print("================================")
    print("USER LEFT")
    print("Room:", room_id)
    print("Username:", username)
    print("Current Users:", room_users)
    print("================================")

    # update user list
    emit(
        "room_users",
        room_users.get(room_id, []),
        room=room_id
    )

    # notify room
    emit(
        "user_left",
        {
            "username": username
        },
        room=room_id
    )

    del user_sessions[sid]

# =========================
# SERVER START
# =========================

if __name__ == "__main__":

    socketio.run(
        app,
        debug=True
    )