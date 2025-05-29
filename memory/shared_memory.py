import sqlite3
import json
from datetime import datetime

class SharedMemory:
    def __init__(self, db_path='memory.db'):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS memory (
            conv_id TEXT PRIMARY KEY,
            data TEXT,
            timestamp TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def store(self, conv_id, data):
        timestamp = str(datetime.now())
        data_json = json.dumps(data)
        self.conn.execute("REPLACE INTO memory (conv_id, data, timestamp) VALUES (?, ?, ?)",
                          (conv_id, data_json, timestamp))
        self.conn.commit()

    def retrieve(self, conv_id):
        cursor = self.conn.execute("SELECT data FROM memory WHERE conv_id=?", (conv_id,))
        row = cursor.fetchone()
        return json.loads(row[0]) if row else {}

    def update(self, conv_id, new_data):
        current_data = self.retrieve(conv_id)
        current_data.update(new_data)
        self.store(conv_id, current_data)