from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
import sqlite3
import os
from pathlib import Path

db_dir = Path("db")
db_dir.mkdir(parents=True, exist_ok=True)
db_path = db_dir / "data.sqlite"

conn = sqlite3.connect(db_path, check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS people_counts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        in_count INTEGER,
        out_count INTEGER
    )
''')
conn.commit()

app = Flask(__name__)
CORS(app) # Dev CORS

@app.post("/api/people_counts")
def people_counts():
    try:
        data = request.get_json()
        timestamp = data.get("timestamp", datetime.now().isoformat())
        in_count = int(data.get("in_count", 0))
        out_count = int(data.get("out_count", 0))

        cursor.execute('''
            INSERT INTO people_counts (timestamp, in_count, out_count)
            VALUES (?, ?, ?)
        ''', (timestamp, in_count, out_count))
        conn.commit()

        return jsonify({"status": "success", "message": "Data inserted"}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.get("/api/people_count_last_10x10min")
def get_people_count_last_10x10min():
    try:
        cursor.execute('SELECT timestamp FROM people_counts ORDER BY timestamp DESC LIMIT 1')
        latest_row = cursor.fetchone()

        if not latest_row:
            return jsonify(content={"status": "success", "data": [], "message": "No data found"}, status_code=200)

        latest_ts_str = latest_row[0]
        latest_ts = datetime.fromisoformat(latest_ts_str)

        data = []

        for i in range(10):
            end_time = latest_ts - timedelta(minutes=10 * i)
            start_time = end_time - timedelta(minutes=10)

            cursor.execute('''
                SELECT SUM(in_count), SUM(out_count)
                FROM people_counts
                WHERE timestamp > ? AND timestamp <= ?
            ''', (start_time.isoformat(), end_time.isoformat()))

            result = cursor.fetchone()
            in_sum = result[0] or 0
            out_sum = result[1] or 0

            data.append({
                "timestamp": end_time.strftime("%Y-%m-%d %H:%M:%S"),
                "in_count": in_sum,
                "out_count": out_sum,
                "onboard": max(in_sum - out_sum, 0)
            })

        data.reverse()

        return jsonify(content={"status": "success", "data": data}, status_code=200)

    except Exception as e:
        return jsonify(content={"status": "error", "message": str(e)}, status_code=400)

@app.get("/api/get_people_count")
def get_people_count():
    try:
        cursor.execute('''
            SELECT timestamp, in_count, out_count
            FROM people_counts
            ORDER BY timestamp DESC
            LIMIT 1
        ''')
        row = cursor.fetchone()

        if row:
            result = {
                "timestamp": row[0],
                "in_count": row[1],
                "out_count": row[2],
                "onboard": row[1] - row[2] if row[1] - row[2] > 0 else 0
            }
            return jsonify({"status": "success", "data": result}), 200
        else:
            return jsonify({"status": "success", "data": None, "message": "No data found"}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400
