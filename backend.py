from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['GET', 'POST'])
def process_data():
    if request.method == 'POST':
        print("Received a POST request.")
        data = request.json
        print(f"Data received: {data}")
        user_id = data.get('user_id')
        college_email = data.get('college_email')
        college_roll_number = data.get('college_roll_number')
        numbers = data.get('numbers', [])
        alphabets = data.get('alphabets', [])
        
        # Find the highest lowercase alphabet
        lowercase_alphabets = [ch for ch in alphabets if ch.islower()]
        highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else None
        
        response = {
            'status': 'success',
            'user_id': user_id,
            'college_email': college_email,
            'college_roll_number': college_roll_number,
            'numbers': numbers,
            'alphabets': alphabets,
            'highest_lowercase': highest_lowercase
        }
        
        return jsonify(response)
    
    elif request.method == 'GET':
        print("Received a GET request.")
        return jsonify({'message': 'Send a POST request with JSON data.'})

if __name__ == '__main__':
    app.run(debug=True)
