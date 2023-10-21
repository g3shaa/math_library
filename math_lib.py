# Constants
PI = 3.14159265358979323846
EULER_NUMBER = 2.71828182845904523536

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def minus(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

# Function to calculate sine (sin) using a Taylor series expansion
def sin(x):
    x = x % (2 * PI)  # Ensure x is in the range [0, 2*pi]
    result = x
    term = x
    i = 1
    while True:
        term *= -x**2 / ((2 * i) * (2 * i + 1)) 
        if term == 0:
            break
        result += term
        i += 1
    return result

# Function to calculate cosine (cos) using a Taylor series expansion
def cos(x):
    x = x % (2 * PI)  # Ensure x is in the range [0, 2*pi]
    result = 1
    term = 1
    i = 1
    while True:
        term *= -x**2 / ((2 * i - 1) * (2 * i))
        if term == 0:
            break
        result += term
        i += 1
    return result

# Function to calculate tangent (tan) as sin(x) / cos(x)
def tan(x):
    return sin(x) / cos(x)

# Function to calculate cotangent (cot) as 1 / tan(x)
def cot(x):
    return 1 / tan(x)

# Function to calculate arcsine (asin) using a Taylor series expansion
def asin(x):
    result = x
    term = x
    i = 1
    while True:
        term *= (x**2 * (2 * i - 1)**2) / ((2 * i) * (2 * i + 1))
        if term == 0:
            break
        result += term
        i += 1
    return result

# Function to calculate arccosine (acos) as pi/2 - asin(x)
def acos(x):
    return PI / 2 - asin(x)

# Function to calculate arctangent (atan) using a Taylor series expansion
def atan(x):
    result = x
    term = x
    i = 1
    while True:
        term *= -x**2 / ((2 * i + 1))
        if term == 0:
            break
        result += term
        i += 1
    return result

# Function to calculate the factorial of a number
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Class for basic geometric calculations
class Geometry:
    @staticmethod
    def area_of_rectangle(length, width):
        return length * width

    @staticmethod
    def area_of_circle(radius):
        return PI * (radius ** 2)

    @staticmethod
    def area_of_triangle(base, height):
        return 0.5 * base * height

# Function to add two complex numbers
def add_complex(z1, z2):
    real_part = z1.real + z2.real
    imag_part = z1.imag + z2.imag
    return complex(real_part, imag_part)

# Function to subtract two complex numbers
def subtract_complex(z1, z2):
    real_part = z1.real - z2.real
    imag_part = z1.imag - z2.imag
    return complex(real_part, imag_part)

# Function to multiply two complex numbers
def multiply_complex(z1, z2):
    real_part = (z1.real * z2.real) - (z1.imag * z2.imag)
    imag_part = (z1.real * z2.imag) + (z2.real * z1.imag)
    return complex(real_part, imag_part)

# Function to divide two complex numbers
def divide_complex(z1, z2):
    denominator = (z2.real ** 2 + z2.imag ** 2)
    real_part = ((z1.real * z2.real) + (z1.imag * z2.imag)) / denominator
    imag_part = ((z1.imag * z2.real) - (z1.real * z2.imag)) / denominator
    return complex(real_part, imag_part)

# Function to calculate the determinant of a 2x2 matrix
def determinant_2x2(matrix):
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        raise ValueError("Input must be a 2x2 matrix")
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

# Function to calculate the determinant of a square matrix (NxN)
def determinant(matrix):
    size = len(matrix)
    if size == 2:
        return determinant_2x2(matrix)
    elif size < 2:
        raise ValueError("Matrix is too small to calculate the determinant")
    else:
        det = 0
        for col in range(size):
            minor = [row[:col] + row[col+1:] for row in matrix[1:]]
            det += matrix[0][col] * determinant(minor) * (-1) ** col
        return det


# Function to calculate the definite integral of a function f(x) using the trapezoidal rule
def definite_integral_trapezoidal(f, a, b, n):
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral

# Function to calculate the indefinite integral of a function f(x) using the power rule
def indefinite_integral_power_rule(f, C=0):
    def integral(x):
        return (f(x) / 2) + C
    return integral


# Function to evaluate a polynomial P(x) with coefficients coefs at a specific value x
def evaluate_polynomial(coefs, x):
    result = 0
    for i, coef in enumerate(coefs):
        result += coef * (x ** i)
    return result

# Function to calculate the derivative of a polynomial P(x) with coefficients coefs
def derivative_of_polynomial(coefs):
    if len(coefs) < 2:
        return [0]
    return [i * coefs[i] for i in range(1, len(coefs))]

# Function to calculate the integral of a polynomial P(x) with coefficients coefs
def integral_of_polynomial(coefs, C=0):
    result = [C]  # Constant of integration
    for i, coef in enumerate(coefs):
        result.append(coef / (i + 1))
    return result   