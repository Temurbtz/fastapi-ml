def sqrt(x: float, tolerance: float = 1e-10) -> float:
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    if x == 0:
        return 0.0
    
    guess = x / 2.0
    
    while True:
        next_guess = (guess + x / guess) / 2.0
        if abs(next_guess - guess) < tolerance:
            return next_guess
        
        guess = next_guess
try:
    number = float(input("Enter a number to compute its square root: "))
    result = sqrt(number)
    print(f"The square root of {number} is approximately {result}")
except ValueError as e:
    print(e)
