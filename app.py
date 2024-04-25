from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

# Function to calculate the dot product of two vectors
def dot_product(vector1, vector2):
    return sum(a * b for a, b in zip(vector1, vector2))

# Function to calculate the length (norm) of a vector
def vector_length(vector):
    return math.sqrt(sum(a**2 for a in vector))

# Function to calculate the angle between two vectors
def vector_angle(vector1, vector2):
    dot_product_val = dot_product(vector1, vector2)
    length1 = vector_length(vector1)
    length2 = vector_length(vector2)
    return math.degrees(math.acos(dot_product_val / (length1 * length2)))

# Function to calculate the distance between two points
def distance_between_points(point1, point2):
    squared_distance = sum((a - b)**2 for a, b in zip(point1, point2))
    return math.sqrt(squared_distance)

@app.route('/<name>')
def index(name):
    return render_template('a.html',name=name)

@app.route('/calculate', methods=['POST'])
def calculate():
    vector_1 = [int(x) for x in request.form['vector_1'].split(',')]
    vector_2 = [int(x) for x in request.form['vector_2'].split(',')]
    point_1 = [int(x) for x in request.form['point_1'].split(',')]
    point_2 = [int(x) for x in request.form['point_2'].split(',')]

 
    length_vector_1 = vector_length(vector_1)
    

    angle_vectors = vector_angle(vector_1, vector_2)
    
    
    distance_points = distance_between_points(point_1, point_2)

    return render_template('result.html', length_vector_1=length_vector_1, angle_vectors=angle_vectors, distance_points=distance_points)

if __name__ == '__main__':
    app.run(debug=True)
