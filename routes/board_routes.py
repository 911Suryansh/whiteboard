from flask import Blueprint, request, jsonify
from services.board_service import BoardService
board_bp = Blueprint("board_bp", __name__)


@board_bp.route("/rooms/<int:room_id>/board", methods=["GET"])
def get_board(room_id):

    result = BoardService.get_board(room_id)

    return jsonify(result)

@board_bp.route("/rooms/<int:room_id>/board", methods=["PATCH"])
def save_board(room_id):

    data = request.get_json()

    board_data = data.get("board")

    result = BoardService.save_board(room_id, board_data)

    return jsonify(result)
