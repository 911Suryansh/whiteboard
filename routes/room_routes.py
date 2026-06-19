from flask import Blueprint, request, jsonify
from services.room_service import RoomService
room_bp = Blueprint("room_bp", __name__)

@room_bp.route("/rooms", methods=["POST"])
def create_room():

    data = request.get_json()

    name = data.get("name")
    username = data.get("username")

    result = RoomService.create_room(name, username)

    return jsonify(result)

@room_bp.route("/rooms", methods=["GET"])
def get_rooms():

    result = RoomService.get_rooms()

    return jsonify(result)

@room_bp.route("/rooms/join", methods=["POST"])
def join_room():

    data = request.get_json()

    code = data.get("code")
    username = data.get("username")

    result = RoomService.join_room(code, username)

    return jsonify(result)