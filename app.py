from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        expression = request.json.get('expression', '')
        result = eval(expression)  # Use a safer eval function in production!
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": "Invalid Input"})

