from largest_number import largest_number_naive
from largest_number import largest_number
from change import change
from fractional_knapsack import optimal_value
from car_fueling import min_refills
from dot_product import max_dot_product, max_dot_product_naive
from covering_segments import optimal_points
from different_summands import optimal_summands

from collections import namedtuple
import unittest
import random

class TestMySolutions(unittest.TestCase):
    def test_change(self):
        self.assertEqual(change(2), 2)
        self.assertEqual(change(28), 6)
        self.assertEqual(change(0), 0)
        self.assertEqual(change(1), 1)
        self.assertEqual(change(100),10)
        self.assertEqual(change(1000), 100)
        self.assertEqual(change(49), 9)

    def test_largest_number(self):
        self.assertEqual(largest_number([1, 1, 1, 1]), "1111")
        self.assertEqual(largest_number([1, 2, 3, 4]), "4321")
        self.assertEqual(largest_number([21, 2]), "221")
        self.assertEqual(largest_number([9, 4, 6, 1, 9]), "99641")
        self.assertEqual(largest_number([23, 39, 92]), "923923")
        self.assertEqual(largest_number([3, 30, 34, 5, 9]), "9534330")
        self.assertEqual(largest_number([94, 61, 34, 67, 9, 4, 3, 8]), "994867614343")
        self.assertEqual(largest_number([1, 100, 100]), "1100100")
        self.assertEqual(largest_number([1, 10, 100, 100]), "110100100")
        self.assertEqual(largest_number([2, 1, 100, 100]), "21100100")
        self.assertEqual(largest_number([2, 21, 25, 1, 100, 100]), "252211100100")
        
    def test_optimal_value(self):
        self.assertAlmostEqual(optimal_value(50, [20,50,30], [60,100,120]), 180.0000)
        self.assertAlmostEqual(optimal_value(10, [30], [500]), 166.6667)
        self.assertAlmostEqual(optimal_value(0, [0], [0]),0)
        self.assertAlmostEqual(optimal_value(1, [int(10e6)], [int(10e6)]), 1)

    def test_min_refills(self):
        self.assertEqual(min_refills(950,400,[200,375,550,750]), 2)
        self.assertEqual(min_refills(200, 250 ,[100,150]), 0)
        self.assertEqual(min_refills(10, 3, [1,2,5,9]), -1 )
        for _ in range(1000): # happy path
            distance = random.randint(1, 100000)
            tank = random.randint(1, 400)
            num_stops = random.randint(2, 301)
            distance_per_stop = distance // num_stops
            stops = [i * distance_per_stop for i in range(num_stops)]
            print("distances in between each stop: ", distance_per_stop)
            print(f"distance: {distance}, tank: {tank}, num_stops:{num_stops}")
            expected = None
            if tank >= distance_per_stop and distance - stops[-1] <= tank:
                expected = distance // tank 
            else:
                expected = -1
            self.assertEqual(min_refills(distance, tank, stops), expected)
            
    def test_max_dot_product(self):
        self.assertEqual(max_dot_product_naive([23],[39]), 897)
        self.assertEqual(max_dot_product_naive([2, 3, 9],[7, 4, 2]), 79)
        for _ in range(10):
            n = random.randint(1, 10)
            prices = [random.randint(0,100) for _ in range(n)]
            clicks = [random.randint(0,100) for _ in range(n)]
            #print(f"prices: {prices}, clicks: {clicks}")
            self.assertEqual(max_dot_product(prices, clicks), max_dot_product_naive(prices, clicks))
        for _ in range(100):
            n = random.randint(1, 10000)
            prices = [random.randint(0,10000) for _ in range(n)]
            clicks = [random.randint(0,10000) for _ in range(n)]
            self.assertIsNotNone(max_dot_product(prices, clicks))

    """def test_optimal_points(self):
        Segment = namedtuple('Segment', 'start end')
        self.assertEqual(optimal_points([Segment(1,3),Segment(2,5), Segment(3,6)]), [3])
        self.assertEqual(optimal_points([Segment(1,3),Segment(2,5), Segment(5,6), Segment(4,7)]), [5,3])
        self.assertEqual(optimal_points([]), [])
        for _ in range(10):
            num_segments = random.randint(1,100)
            segments = []
            for _ in range(num_segments):
                a, b = random.randint(0,int(10e9)), random.randint(0,int(10e9))
                left, right = min(a,b), max(a,b)
                segments.append(Segment(left,right))
            self.assertIsNotNone(optimal_points(segments))"""

    def test_optimal_summands(self):
        self.assertEqual(optimal_summands(6), [1,2,3])
        self.assertEqual(optimal_summands(8), [1,2,5])
        self.assertEqual(optimal_summands(2), [2])

if __name__ == '__main__':
    unittest.main()