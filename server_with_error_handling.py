from flask import Flask, render_template, request, jsonify
# Import the Maths package here
from Maths.mathematics import summation, substraction, multiplication

app = Flask("Mathematics Problem Solver")

def validate_numeric_input(num):
    try:
        return float(num)
    except ValueError:
        return None

@app.route("/sum")
def sum_route():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')

    num1 = validate_numeric_input(num1)
    num2 = validate_numeric_input(num2) 

    # Error handling code
    if num1 is None or num2 is None:
        return jsonify({"error": "Invalid input, please enter valid numbers for num1 and num2"})

    # Write your code here
    result = summation(num1, num2)
    return str(result)

@app.route("/sub")
def sub_route():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')

    num1 = validate_numeric_input(num1)
    num2 = validate_numeric_input(num2) 

    # Error handling code
    if num1 is None or num2 is None:
        return jsonify({"error": "Invalid input, please enter valid numbers for num1 and num2"})

    # Write your code here
    result = substraction(num1, num2)
    return str(result)

@app.route("/mul")
def mul_route():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')

    num1 = validate_numeric_input(num1)
    num2 = validate_numeric_input(num2) 

    # Error handling code
    if num1 is None or num2 is None:
        return jsonify({"error": "Invalid input, please enter valid numbers for num1 and num2"})

    # Write your code here  
    result = multiplication(num1, num2)
    return str(result)

@app.route("/")
def render_index_page():
    # Write your code here
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
