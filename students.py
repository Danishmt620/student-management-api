from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "James", "age": 20, "college": "ABC College", "branch": "Computer Science"},
    {"id": 2, "name": "John", "age": 21, "college": "XYZ College", "branch": "IT"}
]

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

if __name__ == '__main__':
    app.run(debug=True)