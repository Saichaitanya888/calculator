from flask import Flask, render_template, request

app = Flask(__name__)

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to generate Fibonacci series up to n terms
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Function to calculate cube root
def cube_root(num):
    return round(num ** (1/3), 2)

# Function to check if a number is palindrome
def is_palindrome(num):
    return str(num) == str(num)[::-1]

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    prime_result = None
    fibonacci_result = None
    cube_root_result = None
    palindrome_result = None

    if request.method == 'POST':
        number = request.form['number']
        
        # Handle Prime Number Check
        if 'prime' in request.form:
            prime_result = is_prime(int(number))

        # Handle Fibonacci Series
        if 'fibonacci' in request.form:
            fibonacci_result = fibonacci(int(number))

        # Handle Cube Root
        if 'cube_root' in request.form:
            cube_root_result = cube_root(float(number))

        # Handle Palindrome Check
        if 'palindrome' in request.form:
            palindrome_result = is_palindrome(number)

    return render_template('index.html', prime_result=prime_result,
                           fibonacci_result=fibonacci_result,
                           cube_root_result=cube_root_result,
                           palindrome_result=palindrome_result)

if __name__ == '__main__':
    app.run(debug=True)
