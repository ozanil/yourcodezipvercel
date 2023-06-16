from flask import Flask, render_template
import random

app = Flask(__name__)

error_messages = {
    "SyntaxError": [
        "can't assign to function call",
        "can't assign to literal",
        "invalid syntax",
        "'break' outside loop",
        "'continue' not properly in loop",
        "EOL while scanning string literal"
    ],
    "NameError": [
        "name 'variable' is not defined",
        "name 'function' is not defined",
        "name 'module' is not defined",
        "name 'attribute' is not defined",
        "name 'class' is not defined"
    ],
    "TypeError": [
        "unsupported operand type(s) for +: 'int' and 'str'",
        "object of type 'NoneType' has no attribute 'attribute'",
        "can't multiply sequence by non-int of type 'float'",
        "unsupported operand type(s) for /: 'str' and 'int'",
        "argument must be a string or a number, not 'list'"
    ],
    "ValueError": [
        "invalid literal for int() with base 10",
        "could not convert string to float: 'abc'",
        "substring not found",
        "invalid literal for bool() with value '0'",
        "invalid literal for complex() with value 'abc+def'"
    ],
    # Add more error categories and messages as needed
}

@app.route('/')
def show_error():
    error_category = random.choice(list(error_messages.keys()))
    random_error = random.choice(error_messages[error_category])
    title = error_category
    # countdown 5'den geriye sayar ve sayfa yenilenir.

    countdown = 5
    refresh_current_page()

    return render_template('error.html', error=title + ': ' + random_error, title=title, message=f"Your Code will be try debug in {countdown} seconds.")

def refresh_current_page():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)