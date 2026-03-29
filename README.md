# mystery_module

Purpose
-------
`mystery_module.py` provides a small utility for solving quadratic equations of the form
ax² + bx + c = 0 and returning the real roots when they exist.

Functions
---------
- `fn_x(a, b, c)`
  - Description: Compute the real roots of the quadratic equation `a*x**2 + b*x + c = 0`.
  - Inputs: numeric values for `a`, `b`, and `c` (int or float).
  - Output: Returns a tuple `(r1, r2)` of floats when the discriminant is non-negative; returns `None` when there are no real roots.
  - Exceptions: A `ZeroDivisionError` occurs when `a == 0` (not a quadratic). Non-numeric inputs will raise the underlying type conversion/operation errors.

Examples
--------
```python
from mystery_module import fn_x

print(fn_x(1, -3, 2))   # -> (2.0, 1.0)
print(fn_x(1, 2, 5))    # -> None (no real roots)
print(fn_x(1, 2, 1))    # -> (-1.0, -1.0) (double root)
```

Assumptions and Limitations
---------------------------
- The function expects `a` to be non-zero for a proper quadratic equation. If you need to handle the linear case (`a == 0`), handle it before calling `fn_x` or extend the function.
- Complex roots are not returned; the function returns `None` when the discriminant is negative. If complex roots are required, consider using `cmath.sqrt` and returning complex values.
- There is no input validation beyond relying on Python operations — callers should ensure inputs are numeric.

Suggestions for improvement
---------------------------
- Add a docstring and type hints to `fn_x` for clarity.
- Handle `a == 0` explicitly (solve linear equation or raise a clearer error).
- Optionally provide an argument to return complex roots when requested.

License / Notes
---------------
This module is minimal and intended for simple, illustrative use. Adapt for production use by adding validation, tests, and better error messages.
