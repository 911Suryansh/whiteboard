from config.extension import mysql


class RoomModel:

    @staticmethod
    def create_room(name, room_code):

        cur = mysql.connection.cursor()

        cur.execute("""
            INSERT INTO rooms (name, room_code)
            VALUES (%s, %s)
        """, (name, room_code))

        mysql.connection.commit()

        room_id = cur.lastrowid

        cur.close()

        return room_id 
    
    @staticmethod
    def get_all_rooms():

        cur = mysql.connection.cursor()

        cur.execute("""
            SELECT id, name, room_code, created_at
            FROM rooms
            ORDER BY created_at DESC
        """)

        rows = cur.fetchall()

        cur.close()

        return rows
    
    @staticmethod
    def get_room_by_code(code):

        cur = mysql.connection.cursor()

        cur.execute("""
            SELECT id, name, room_code
            FROM rooms
            WHERE room_code = %s
        """, (code,))

        row = cur.fetchone()

        cur.close()

        return row
    
    @staticmethod
    def get_room_by_id(room_id):

        cur = mysql.connection.cursor()

        cur.execute("""
            SELECT id, name, room_code
            FROM rooms
            WHERE id = %s
        """, (room_id,))

        row = cur.fetchone()

        cur.close()

        return row