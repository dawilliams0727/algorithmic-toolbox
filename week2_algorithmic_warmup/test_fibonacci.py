import random
from fibonacci import fibonacci_number, fibonacci_number_fast
from fibonacci_last_digit import fibonacci_last_digit, fibonacci_last_digit_fast
from fibonacci_huge import fibonacci_huge_fast
from fibonacci_sum_last_digit import fibonacci_sum, fibonacci_sum_fast
from fibonacci_partial_sum import fibonacci_partial_sum_naive, fibonacci_partial_sum_fast
from fibonacci_sum_squares import fibonacci_sum_squares, fibonacci_sum_squares_fast
from lcm import lcm, lcm_fast
from gcd import gcd, gcd_fast
import unittest

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_number(self):
        self.assertEqual(fibonacci_number(0), 0)
        self.assertEqual(fibonacci_number(1), 1)
        self.assertEqual(fibonacci_number(2), 1)
        self.assertEqual(fibonacci_number(3), 2)
        self.assertEqual(fibonacci_number(10), 55)
    
    def test_fibonacci_number_fast(self):
        self.assertEqual(fibonacci_number_fast(0), fibonacci_number(0))
        self.assertEqual(fibonacci_number_fast(1), fibonacci_number(1))
        self.assertEqual(fibonacci_number_fast(2), fibonacci_number(2))
        self.assertEqual(fibonacci_number_fast(3), fibonacci_number(3))
        self.assertEqual(fibonacci_number_fast(10), 55)
        self.assertEqual(fibonacci_number_fast(30), 832040)
        self.assertEqual(fibonacci_number_fast(33), 3524578)
        self.assertEqual(fibonacci_number_fast(35), 9227465)
        self.assertEqual(fibonacci_number_fast(40), 102334155)
        self.assertEqual(fibonacci_number_fast(45), 1134903170)

    def test_fibonacci_last_digit(self):
        self.assertEqual(fibonacci_last_digit(0), 0)
        self.assertEqual(fibonacci_last_digit(3), 2)
        self.assertEqual(fibonacci_last_digit(139), 1)
        self.assertEqual(fibonacci_last_digit(91239), 6)
    
    def test_fibonacci_last_digit_fast(self):
        self.assertEqual(fibonacci_last_digit_fast(0), fibonacci_last_digit(0))
        self.assertEqual(fibonacci_last_digit_fast(3), fibonacci_last_digit(3))
        self.assertEqual(fibonacci_last_digit_fast(139), fibonacci_last_digit(139))
        self.assertEqual(fibonacci_last_digit_fast(91239), fibonacci_last_digit(91239))
        self.assertEqual(fibonacci_last_digit_fast(int(10e6)), 5)

    def test_fibonacci_huge(self):
        self.assertEqual(fibonacci_huge_fast(1, 239), 1)
        self.assertEqual(fibonacci_huge_fast(115, 1000), 885)
        self.assertEqual(fibonacci_huge_fast(2816213588, 239), 151)
        self.assertTrue(fibonacci_huge_fast(int(10e14), 100000).is_integer())

    def test_fibonacci_sum(self):
        for _ in range(100):
            n = random.randint(1, 1000)
            self.assertEqual(fibonacci_sum(n), fibonacci_sum_fast(n))
        self.assertEqual(fibonacci_sum_fast(0), 0)
        self.assertEqual(fibonacci_sum_fast(3), 4)
        self.assertEqual(fibonacci_sum_fast(100), 5)
        self.assertEqual(fibonacci_sum_fast(int(10e14)), 5)
        
    def test_fibonacci_partial_sum(self):
        for i in range(1000):
            a,b =  random.randint(1, 10000), random.randint(1, 10000)
            from_, to = min(a,b), max(a,b)
            self.assertEqual(fibonacci_partial_sum_naive(from_, to), fibonacci_partial_sum_fast(from_, to))
        self.assertEqual(fibonacci_partial_sum_fast(3, 7), 1)
        self.assertEqual(fibonacci_partial_sum_fast(3, 7), 1)
        self.assertEqual(fibonacci_partial_sum_fast(0, 0), 0)
        self.assertTrue(fibonacci_partial_sum_fast(10, int(10e14)).is_integer())
        
    def test_fibonacci_sum_squares(self):
        self.assertEqual(fibonacci_sum_squares(0), 0)
        self.assertEqual(fibonacci_sum_squares(7), 3)
        self.assertEqual(fibonacci_sum_squares(73), 1)
        for _ in range(100):
            n = random.randint(1, 1000)
            self.assertEqual(fibonacci_sum_squares(n), fibonacci_sum_squares_fast(n))
        self.assertEqual(fibonacci_sum_squares_fast(0), 0)
        self.assertEqual(fibonacci_sum_squares_fast(7), 3)
        self.assertEqual(fibonacci_sum_squares_fast(73), 1)
        self.assertEqual(fibonacci_sum_squares_fast(1234567890), 0)
        self.assertEqual(fibonacci_sum_squares_fast(100000000000000), 5)

    def test_gcd(self):
        self.assertEqual(gcd(6, 8), 2)
        self.assertEqual(gcd( 28851538, 1183019), 17657)
        for _ in range (1000):
            a, b = random.randint(1, 10000), random.randint(1, 10000)
            low, high = min(a,b), max(a,b)
            self.assertEqual(gcd(low, high), gcd_fast(low, high))
        self.assertEqual(gcd_fast(6, 8), 2)
        self.assertEqual(gcd_fast( 28851538, 1183019), 17657)
        self.assertTrue(gcd_fast(2, int(2e9)).is_integer())
    
    def test_lcm(self):
        self.assertEqual(lcm(15, 8), 120)
        self.assertEqual(lcm(15, 6), 30)
        self.assertEqual(lcm(8, 6), 24)
        for _ in range(100):
            a, b = random.randint(1, 1000), random.randint(1, 1000)
            self.assertEqual(lcm(a, b), lcm_fast(a, b))
        self.assertEqual(lcm_fast(15, 8), 120)
        self.assertEqual(lcm_fast(15, 6), 30)
        self.assertEqual(lcm(8, 6), 24)
        self.assertTrue(lcm_fast(1, int(10e7)).is_integer())


#1000000000000000000
#2000000000

if __name__ == '__main__':
    unittest.main()