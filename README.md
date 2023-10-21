<h1>Technical Documentation</h1>

<h2>Introduction</h2>

<p>This technical documentation provides an overview of a Python project that includes a collection of mathematical and
    geometric functions. The project contains mathematical constants, basic arithmetic operations, trigonometric and
    inverse trigonometric functions, complex number operations, geometric calculations, integral functions, polynomial
    functions, and more.</p>

<h2>Constants</h2>

<p>The project defines several mathematical constants:</p>

<ul>
    <li><strong>PI (π):</strong> Approximated as 3.14159265358979323846.</li>
    <li><strong>EULER_NUMBER (e):</strong> Approximated as 2.71828182845904523536.</li>
    <li><strong>INFINITY:</strong> Represents positive infinity.</li>
    <li><strong>NAN (Not-a-Number):</strong> Represents a value that is not a number.</li>
    <li><strong>HUGE_VAL, HUGE_VALF, HUGE_VALL:</strong> Constants representing positive infinity (for different
        floating-point types).</li>
</ul>

<h2>Basic Arithmetic Operations</h2>

<p>The project includes functions for basic arithmetic operations:</p>

<h3><code>add(x, y)</code></h3>

<p>This function adds two numbers <code>x</code> and <code>y</code> and returns the result.</p>

<h3><code>minus(x, y)</code></h3>

<p>This function subtracts <code>y</code> from <code>x</code> and returns the result.</p>

<h3><code>multiply(x, y)</code></h3>

<p>This function multiplies two numbers <code>x</code> and <code>y</code> and returns the result.</p>

<h3><code>divide(x, y)</code></h3>

<p>This function divides <code>x</code> by <code>y</code> and returns the result. It raises a <code>ValueError</code> if
    <code>y</code> is equal to 0 (division by zero).</p>

<h2>Trigonometric Functions</h2>

<p>The project provides trigonometric functions:</p>

<h3><code>sin(x)</code></h3>

<p>Calculates the sine of <code>x</code> using a Taylor series expansion. The function ensures that <code>x</code> is
    within the range [0, 2π].</p>

<h3><code>cos(x)</code></h3>

<p>Calculates the cosine of <code>x</code> using a Taylor series expansion. The function ensures that <code>x</code> is
    within the range [0, 2π].</p>

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

<h2>Hyperbolic Functions</h2>

<p>The project also includes hyperbolic functions:</p>

<h3><code>cosh(x)</code></h3>

<p>Calculates the hyperbolic cosine of <code>x</code>.</p>

<h3><code>sinh(x)</code></h3>

<p>Calculates the hyperbolic sine of <code>x</code>.</p>

<h3><code>tanh(x)</code></h3>

<p>Calculates the hyperbolic tangent of <code>x</code>.</p>

<h3><code>acosh(x)</code></h3>

<p>Calculates the inverse hyperbolic cosine of <code>x</code>.</p>

<h3><code>asinh(x)</code></h3>

<p>Calculates the inverse hyperbolic sine of <code>x</code>.</p>

<h3><code>atanh(x)</code></h3>

<p>Calculates the inverse hyperbolic tangent of <code>x</code>.</p>

<h2>Exponential and Logarithmic Functions</h2>

<p>Exponential and logarithmic functions are also available:</p>

<h3><code>exp(x)</code></h3>

<p>Calculates the exponential function of <code>x</code>.</p>

<h3><code>log(x)</code></h3>

<p>Calculates the natural logarithm of <code>x</code>.</p>

<h3><code>log10(x)</code></h3>

<p>Calculates the base-10 logarithm of <code>x</code>.</p>

<h3><code>pow(x, y)</code></h3>

<p>Calculates <code>x</code> raised to the power of <code>y</code>.</p>

<h3><code>sqrt(x)</code></h3>

<p>Calculates the square root of <code>x</code>.</p>

<h3><code>cbrt(x)</code></h3>

<p>Calculates the cube root of <code>x</code>.</p>

<h3><code>hypot(x, y)</code></h3>

<p>Calculates the hypotenuse of a right triangle with legs of length <code>x</code> and <code>y</code>.</p>

<h2>Error and Gamma Functions</h2>

<p>The project provides error and gamma functions:</p>

<h3><code>erf(x)</code></h3>

<p>Calculates the error function of <code>x</code>.</p>

<h3><code>erfc(x)</code></h3>

<p>Calculates the complementary error function of <code>x</code>.</p>

<h3><code>tgamma(x)</code></h3>

<p>Calculates the gamma function of <code>x</code>.</p>

<h3><code>lgamma(x)</code></h3>

<p>Calculates the natural logarithm of the absolute value of the gamma function of <code>x</code>.</p>

<h2>Rounding and Remainder Functions</h2>

<p>Rounding and remainder functions are also included:</p>

<h3><code>ceil(x)</code></h3>

<p>Rounds <code>x</code> up to the nearest integer.</p>

<h3><code>floor(x)</code></h3>

<p>Rounds <code>x</code> down to the nearest integer.</p>

<h3><code>fmod(x, y)</code></h3>

<p>Calculates the remainder of the division of <code>x</code> by <code>y</code>.</p>

<h3><code>trunc(x)</code></h3>

<p>Rounds <code>x</code> towards zero to the nearest integer.</p>

<h3><code>round(x)</code></h3>

<p>Rounds <code>x</code> to the nearest integer using "round half to even" rounding.</p>

<h2>Floating-Point Manipulation Functions</h2>

<p>Functions for manipulating floating-point values:</p>

<h3><code>copysign(x, y)</code></h3>

<p>Returns the absolute value of <code>x</code> with the sign of <code>y</code>.</p>

<h3><code>nan(x)</code></h3>

<p>Returns a quiet NaN (Not-a-Number) with a payload of <code>x</code>.</p>

<h3><code>fdim(x, y)</code></h3>

<p>Returns the positive difference between <code>x</code> and <code>y</code>.</p>

<h3><code>fmax(x, y)</code></h3>

<p>Returns the maximum of <code>x</code> and <code>y</code>.</p>

<h3><code>fmin(x, y)</code></h3>

<p>Returns the minimum of <code>x</code> and <code>y</code>.</p>

<h3><code>signbit(x)</code></h3>

<p>Returns <code>true</code> if the sign bit of <code>x</code> is set (negative), or <code>false</code> if it is not set
    (non-negative).</p>

<h2>Comparison Functions</h2>

<p>Functions for comparing values:</p>

<h3><code>isgreater(x, y)</code></h3>

<p>Returns <code>true</code> if <code>x</code is greater than <code>y</code>.</p>

<h3><code>isgreaterequal(x, y)</code></h3>

<p>Returns <code>true</code> if <code>x</code is greater than or equal to <code>y</code>.</p>

<h3><code>isless(x, y)</code></h3>

<p>Returns <code>true</code> if <code>x</code is less than <code>y</code>.</p>

<h3><code>islessequal(x, y)</code></h3>

<p>Returns <code>true</code> if <code>x</code is less than or equal to <code>y</code>.</p>

<h3><code>islessgreater(x, y)</code></h3>

<p>Returns <code>true</code> if <code>x</code is less than or greater than <code>y</code>.</p>

<h2>Conclusion</h2>

<p>This Python university project provides a comprehensive set of mathematical and geometric functions, along with
    constants and integral functions, that can be used for educational and practical purposes in the fields of
    mathematics, physics, and engineering. The project is organized into clearly defined functions and is designed to be
    a versatile and valuable resource for students and learners.</p>
