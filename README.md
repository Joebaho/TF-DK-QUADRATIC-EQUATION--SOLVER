### QUADRATIC EQUATION SOLVER

This repository contains files and folder for project that  aims to develop and deploy a scalable web application that solves quadratic equations, incorporating modern DevOps practices and cloud infrastructure automation. 
The application will provide users with a simple interface to input coefficients (a, b, c) of a quadratic equation (ax² + bx + c = 0) and receive calculated roots in real-time.

The technical implementation leverages containerization through Docker for consistent deployment environments, Infrastructure as Code (IaC) using both Terraform and AWS CloudFormation for cloud resource management, and Bash scripting for automation and operational tasks. 
This multi-tool approach demonstrates the integration of various DevOps technologies while solving a practical mathematical problem. 

A robust tool that solves quadratic equations of the form ax² + bx + c = 0. This solver handles real and complex roots, providing detailed solutions with steps.
Features

Solves any quadratic equation in standard form (ax² + bx + c = 0)
Handles all possible cases:

Two distinct real roots
One repeated real root
Two complex roots


Shows detailed step-by-step solution
Validates input coefficients
Handles edge cases (a = 0, undefined solutions)

Installation
bashCopygit clone https://github.com/Joebaho/TF-DK-quadratic-solver.git
cd quadratic-solver
pip install -r requirements.txt
Usage
pythonCopyfrom quadratic_solver import solve_quadratic

# Example: Solve x² + 5x + 6 = 0
roots = solve_quadratic(a=1, b=5, c=6)
print(roots)  # Output: (-2.0, -3.0)

# For step-by-step solution
solution = solve_quadratic(a=1, b=5, c=6, show_steps=True)
Command Line Interface
bashCopypython quadratic_solver.py -a 1 -b 5 -c 6
Input Parameters

a: Coefficient of x²
b: Coefficient of x
c: Constant term
show_steps: Boolean flag for detailed solution (optional)

Output Format
The solver returns a tuple containing:

For real roots: (root1, root2)
For complex roots: (real1 + imag1j, real2 + imag2j)

Examples

Two real roots:
pythonCopy# x² + 5x + 6 = 0
solve_quadratic(1, 5, 6)  # Returns (-2.0, -3.0)

Complex roots:
pythonCopy# x² + 2x + 5 = 0
solve_quadratic(1, 2, 5)  # Returns (-1+2j, -1-2j)

One repeated root:
pythonCopy# x² + 4x + 4 = 0
solve_quadratic(1, 4, 4)  # Returns (-2.0, -2.0)


Error Handling
The solver includes comprehensive error handling for:

Zero coefficient of x² (a = 0)
Invalid input types
Numerical overflow cases
Division by zero

Contributing
Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

Based on the quadratic formula: x = (-b ± √(b² - 4ac)) / (2a)
Special thanks to contributors and math enthusiasts
