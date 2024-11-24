from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Enter Your Date of Birth</h1>
    <form method="POST" action="/calculate_age">
        <label for="dob">Date of Birth (YYYY-MM-DD):</label>
        <input type="date" id="dob" name="dob">
        <button type="submit">Submit</button>
    </form>
    '''

@app.route('/calculate_age', methods=['POST'])
def calculate_age():
    dob_str = request.form.get('dob', '')
    if not dob_str:
        return '''
        <h1>Error: Please provide a valid date of birth.</h1>
        <a href="/">Back</a>
        '''
    try:
        dob = datetime.strptime(dob_str, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return f'''
        <h1>Your Age: {age} years</h1>
        <a href="/">Back</a>
        '''
    except ValueError:
        return '''
        <h1>Error: Invalid Date Format. Please use YYYY-MM-DD.</h1>
        <a href="/">Back</a>
        '''

if __name__ == '__main__':
    app.run(debug=True)
