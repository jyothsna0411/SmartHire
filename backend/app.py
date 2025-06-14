from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://mongodb:27017/smarthire')
client = MongoClient(MONGO_URI)
db = client.smarthire

@app.route('/')
def home():
    return jsonify({"message": "SmartHire API running"})

@app.route('/health')
def health():
    try:
        db.jobs.find_one()
        return jsonify({"status": "healthy"})
    except:
        return jsonify({"status": "unhealthy"}), 500

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    jobs = list(db.jobs.find({}, {'_id': 0}))
    return jsonify({"jobs": jobs})

@app.route('/api/jobs', methods=['POST'])
def create_job():
    data = request.json
    data['createdAt'] = datetime.now().isoformat()
    db.jobs.insert_one(data)
    return jsonify({"message": "Job created"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
