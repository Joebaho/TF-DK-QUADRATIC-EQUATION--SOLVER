from flask import Flask, render_template, request
from math import sqrt
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("app.log"),  # Log to a file
                        logging.StreamHandler()          # Log to the console
                    ])

app = Flask(__name__)

def resolve_equation_second_degree(a, b, c):
    """
    Solves a second-degree equation of the form ax^2 + bx + c = 0.

    Parameters:
    a (float): Coefficient of x^2 
    b (float): Coefficient of x
    c (float): Constant term

    Returns:
    str: A string describing the nature of the solution and the solution(s).
    If the equation is invalid (a=0 and b=0), it returns an error message.
    """
    try:
        if a == 0:
            if b == 0:
                return "Invalid equation. Both 'a' and 'b' cannot be zero."
            # Linear equation (bx + c = 0)
            x = -c / b
            logging.info(f"Resolved linear equation: a={a}, b={b}, c={c}, solution={x}")
            return f"The solution is x = {x}"
        
        # Quadratic equation (ax^2 + bx + c = 0)
        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = (-b + sqrt(delta)) / (2*a)
            x2 = (-b - sqrt(delta)) / (2*a)
            logging.info(f"Two real solutions: a={a}, b={b}, c={c}, x1={x1}, x2={x2}")
            return f"There are two real solutions: x1 = {x1} and x2 = {x2}"
        elif delta == 0:
            x0 = -b / (2*a)
            logging.info(f"Double solution: a={a}, b={b}, c={c}, x0={x0}")
            return f"There is a double solution: x0 = {x0}"
        else:
            real_part = -b / (2*a)
            imaginary_part = sqrt(-delta) / (2*a)
            logging.info(f"Complex solutions: a={a}, b={b}, c={c}, real_part={real_part}, imaginary_part={imaginary_part}")
            return f"There are two complex solutions: z1 = {real_part} + {imaginary_part}i and z2 = {real_part} - {imaginary_part}i"
    except Exception as e:
        logging.error(f"Error resolving equation: a={a}, b={b}, c={c}, error={str(e)}")
        return "An unexpected error occurred while solving the equation."

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            # Get coefficients from the form
            a = float(request.form['a'])
            b = float(request.form['b'])
            c = float(request.form['c'])
            logging.info(f"Received input: a={a}, b={b}, c={c}")
            
            # Solve the equation
            result = resolve_equation_second_degree(a, b, c)
        except ValueError:
            logging.warning("Invalid input: Non-numeric values entered.")
            result = "Please enter valid numeric values for a, b, and c."
        except Exception as e:
            logging.error(f"Unexpected error: {str(e)}")
            result = "An unexpected error occurred. Please try again."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    logging.info("Starting the Flask application...")
    app.run(host='0.0.0.0', port=5000)
