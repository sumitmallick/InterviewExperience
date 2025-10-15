import unittest
import logging
import functools

logging.basicConfig(level = logging.INFO, format = "%(asctime)s - %(message)s")

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_calls
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n in (0, 1):
        return 1
    return n * (factorial(n-1))

class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)
    
    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)
    
    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)
    
    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-6)

if __name__ == "__main__":
    unittest.main()
    
