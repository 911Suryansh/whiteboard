from models.board_model import BoardModel

class BoardService:

    @staticmethod
    def get_board(room_id):

        board = BoardModel.get_board(room_id)

        if not board:
            return {"board": []}

        return {
            "board": board[0]
        }
    
    @staticmethod
    def save_board(room_id, board_data):

        if not board_data:
            return {"error": "Empty board"}

        BoardModel.update_board(
            room_id,
            board_data
        )

        return {
            "message": "Board saved successfully"
        }