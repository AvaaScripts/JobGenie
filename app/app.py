from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)


# Replace with your actual MongoDB Atlas connection string here
app.config["MONGO_URI"] = "mongodb+srv://ava:ava@project.s0c6u.mongodb.net/jobgenie?retryWrites=true&w=majority&appName=project"

mongo = PyMongo(app)

@app.route('/')
def home():
    return jsonify({"message": "JobGenie API with MongoDB is running!"})

@app.route('/add-job', methods=['POST'])
def add_job():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Insert job data into 'jobs' collection in MongoDB
    result = mongo.db.jobs.insert_one(data)
    return jsonify({
        "message": "Job added successfully!",
        "job_id": str(result.inserted_id)
    })

@app.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = mongo.db.jobs.find()
    job_list = []
    for job in jobs:
        job['_id'] = str(job['_id'])  # convert ObjectId to string for JSON
        job_list.append(job)
    return jsonify(job_list)

if __name__ == '__main__':
    app.run(debug=True)
