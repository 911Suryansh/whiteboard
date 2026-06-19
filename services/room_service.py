from models.room_model import RoomModel
from models.board_model import BoardModel
from models.participant_model import ParticipantModel
from utils.room_code_generator import generate_room_code

class RoomService:

    @staticmethod
    def create_room(name, username):

        # 1. validation
        if not name:
            return {"error": "Room name required"}

        # 2. generate unique code
        room_code = generate_room_code()

        # 3. create room
        room_id = RoomModel.create_room(name, room_code)

        # 4. create empty board
        BoardModel.create_board(room_id)

        # 5. add creator as participant
        ParticipantModel.add_participant(
            room_id,
            username,
            role="owner"
        )

        # 6. return response
        return {
            "room_id": room_id,
            "room_code": room_code
        }
    
    @staticmethod
    def join_room(room_code, username):

        # 1. check room exists
        room = RoomModel.get_room_by_code(room_code)

        if not room:
            return {"error": "Invalid room code"}

        room_id = room[0]

        # 2. add participant
        ParticipantModel.add_participant(
            room_id,
            username,
            role="editor"
        )

        return {
            "room_id": room_id,
            "message": "Joined successfully"
        }
    


    @staticmethod
    def get_rooms():

        rooms = RoomModel.get_all_rooms()

        return rooms