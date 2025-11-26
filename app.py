from flask import Flask, request, jsonify
from students import students

app=Flask(__name__)
# GET all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# GET student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = next((s for s in students if s['id'] == id), None)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student)

# POST - Add new student
@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.get_json()
    new_student['id'] = len(students) + 1
    students.append(new_student)
    return jsonify(new_student), 201

# PATCH - Update student partially
@app.route('/students/<int:id>', methods=['PATCH'])
def update_student(id):
    student = next((s for s in students if s['id'] == id), None)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    
    data = request.get_json()
    student.update({k: v for k, v in data.items() if k in student})
    return jsonify(student)

# DELETE - Remove student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    global students
    student = next((s for s in students if s['id'] == id), None)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    
    students = [s for s in students if s['id'] != id]
    return jsonify(student)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, port=5000)
