import unittest

class TestPrimeFactors(unittest.TestCase):
    
    def test_prime_number(self):
        self.assertEqual(prime_factors(7), [7])
    
    def test_small_number(self):
        self.assertEqual(prime_factors(12), [2, 2, 3])
    
    def test_large_number(self):
        self.assertEqual(prime_factors(3958159172), [2, 2, 11, 2347, 38329])
    
    def test_one(self):
        self.assertEqual(prime_factors(1), [])

def prime_factors(number):
    factors = []
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    return factors

if __name__ == "__main__":
    unittest.main()


