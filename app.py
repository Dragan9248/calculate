from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate')
def calculate():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    operation = request.args.get('operation')
    
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    else:
        result = 'Unknown operation'
    
    return f'{result}'

if __name__ == '__main__':
    app.run(debug=True)