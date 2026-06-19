from config.extension import mysql


class ParticipantModel:

    @staticmethod
    def add_participant(room_id, username, role="editor"):

        cur = mysql.connection.cursor()

        cur.execute("""
            INSERT INTO participants (room_id, username, role)
            VALUES (%s, %s, %s)
        """, (room_id, username, role))

        mysql.connection.commit()

        cur.close()

        return True
    
    
    @staticmethod
    def get_participants(room_id):

        cur = mysql.connection.cursor()

        cur.execute("""
            SELECT username, role
            FROM participants
            WHERE room_id = %s
        """, (room_id,))

        rows = cur.fetchall()

        cur.close()

        return rows