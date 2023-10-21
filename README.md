<h1>Technical Documentation</h1>

<h2>Introduction</h2>

<p>This technical documentation provides an overview of a Python project that includes a collection of mathematical and geometric functions. The project contains mathematical constants, basic arithmetic operations, trigonometric and inverse trigonometric functions, and complex number operations. It also includes geometric calculations for rectangles, circles, and triangles.</p>

<h2>Constants</h2>

<p>The project defines two mathematical constants:</p>

<ul>
    <li><strong>PI (π):</strong> Approximated as 3.14159265358979323846.</li>
    <li><strong>EULER_NUMBER (e):</strong> Approximated as 2.71828182845904523536.</li>
</ul>

<p>These constants are used in various mathematical calculations within the project.</p>

<h2>Basic Arithmetic Operations</h2>

<h3><code>add(x, y)</code></h3>

<p>This function adds two numbers <code>x</code> and <code>y</code> and returns the result.</p>

<h3><code>minus(x, y)</code></h3>

<p>This function subtracts <code>y</code> from <code>x</code> and returns the result.</p>

<h3><code>multiply(x, y)</code></h3>

<p>This function multiplies two numbers <code>x</code> and <codey></code> and returns the result.</p>

<h3><code>divide(x, y)</code></h3>

<p>This function divides <code>x</code> by <code>y</code> and returns the result. It raises a <code>ValueError</code> if <code>y</code> is equal to 0 (division by zero).</p>

<h2>Trigonometric Functions</h2>

<h3><code>sin(x)</code></h3>

<p>Calculates the sine of <code>x</code> using a Taylor series expansion. The function ensures that <code>x</code> is within the range [0, 2π].</p>

<h3><code>cos(x)</code></h3>

<p>Calculates the cosine of <code>x</code> using a Taylor series expansion. The function ensures that <code>x</code> is within the range [0, 2π].</p>

<h3><code>tan(x)</code></h3>

<p>Calculates the tangent of <code>x</code> as sin(<code>x</code>) / cos(<code>x</code>).</p>

<h3><code>cot(x)</code></h3>

<p>Calculates the cotangent of <code>x</code> as 1 / tan(<code>x</code>).</p>

<h3><code>asin(x)</code></h3>

<p>Calculates the arcsine of <code>x</code> using a Taylor series expansion.</p>

<h3><code>acos(x)</code></h3>

<p>Calculates the arccosine of <code>x</code> as π/2 - asin(<code>x</code>).</p>

<h3><code>atan(x)</code></h3>

<p>Calculates the arctangent of <code>x</code> using a Taylor series expansion.</p>

<h2>Factorial Calculation</h2>

<h3><code>factorial(n)</code></h3>

<p>Calculates the factorial of a non-negative integer <code>n</code>. It raises a <code>ValueError</code> for negative input. If <code>n</code> is 0, it returns 1.</p>

<h2>Geometry Calculations</h2>

<h3><code>Geometry</code></h3>

<p>This class contains static methods for basic geometric calculations:</p>

<ul>
    <li><code>area_of_rectangle(length, width)</code>: Calculates the area of a rectangle.</li>
    <li><code>area_of_circle(radius)</code>: Calculates the area of a circle.</li>
    <li><code>area_of_triangle(base, height)</code>: Calculates the area of a triangle.</li>
</ul>

<h2>Complex Number Operations</h2>

<h3><code>add_complex(z1, z2)</code></h3>

<p>Adds two complex numbers <code>z1</code> and <code>z2</code> and returns the result as a complex number.</p>

<h3><code>subtract_complex(z1, z2)</code></h3>

<p>Subtracts <code>z2</code> from <code>z1</code> and returns the result as a complex number.</p>

<h3><code>multiply_complex(z1, z2)</code></h3>

<p>Multiplies two complex numbers <code>z1</code> and <code>z2</code> and returns the result as a complex number.</p>

<h3><code>divide_complex(z1, z2)</code></h3>

<p>Divides <code>z1</code> by <code>z2</code> and returns the result as a complex number.</p>

<h2>Matrix Determinants</h2>

<h3><code>determinant_2x2(matrix)</code></h3>

<p>Calculates the determinant of a 2x2 matrix.</p>

<h3><code>determinant(matrix)</code></h3>

<p>Calculates the determinant of a square matrix of size NxN. This function recursively calculates the determinant for larger matrices by applying the Laplace expansion formula.</p>

<h2>Conclusion</h2>

<p>This project provides a rich set of mathematical and geometric functions suitable for various engineering and mathematical applications. This is a university project that includes mathematical constants, basic arithmetic operations, trigonometric functions, complex number operations, and geometric calculations. This resource can be valuable for students and learners studying mathematics, physics, and engineering sciences.




</p>
