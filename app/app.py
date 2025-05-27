from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route to test if it's working
@app.route('/')
def home():
    return jsonify({"message": "JobGenie API is running!"})

@app.route('/add-job',methods=['POST'])
def add_job():
    data=request.get_json()
    return jsonify({
        "message": "Job received successfully!",
        "job_data": data
    })
if __name__ == '__main__':
    app.run(debug=True)

