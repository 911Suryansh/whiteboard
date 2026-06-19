from config.extension import mysql


class BoardModel:

    @staticmethod
    def create_board(room_id):

        cur = mysql.connection.cursor()

        cur.execute("""
            INSERT INTO boards (room_id, board_json)
            VALUES (%s, %s)
        """, (room_id, "[]"))

        mysql.connection.commit()

        cur.close()

        return True
    
    @staticmethod
    def get_board(room_id):

        cur = mysql.connection.cursor()

        cur.execute("""
            SELECT board_json
            FROM boards
            WHERE room_id = %s
        """, (room_id,))

        row = cur.fetchone()

        cur.close()

        return row
    
    @staticmethod
    def update_board(room_id, board_json):

        cur = mysql.connection.cursor()

        cur.execute("""
            UPDATE boards
            SET board_json = %s
            WHERE room_id = %s
        """, (board_json, room_id))

        mysql.connection.commit()

        cur.close()

        return True