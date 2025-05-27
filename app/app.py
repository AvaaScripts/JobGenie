from flask import Flask, jsonify

app = Flask(__name__)

# Home route to test if it's working
@app.route('/')
def home():
    return jsonify({"message": "JobGenie API is running!"})

if __name__ == '__main__':
    app.run(debug=True)

