import random
import unittest
from binary_search import binary_search
from binary_search_duplicates import binary_search_duplicates
#from majority_element import majority_element
from sorting import partition3, randomized_quick_sort
from inversions import inversions, inversions_naive
from points_and_segments import points_cover, points_cover_naive
#from closest import mds, minimum_distance_squared_naive

class TestSolutions(unittest.TestCase):
    def test_binary_search(self):
        test_data = [
            {
                "keys":[1,5,8,12,13],
                "queries":[8,1,23,1,11],
                "expected": [2,0,-1,0,-1]
            },
            {
                "keys":[1],
                "queries":[1],
                "expected": [0]
            },
            {
                "keys":[1],
                "queries":[8],
                "expected": [-1]
            },
            {
                "keys":[1, 10000, int(10e9)],
                "queries":[1,2,125,646532,int(10e9)],
                "expected": [0,-1,-1,-1,2]
            },
            {
                "keys":[1,2,3,4,5],
                "queries":[1,2,3,4,5],
                "expected":[0,1,2,3,4]
            }
        ]
        for _ in range(10):
            num_keys = random.randint(1, int(3*10))
            num_queries = random.randint(1, int(10))
            keys = [random.randint(1, int(10e9)) for _ in range(num_keys)]
            queries = [random.randint(1, int(10e9)) for _ in range(num_queries)]
            expected = []
            for q in queries:
                #print(f"Currently {q}")
                try:
                    expected.append(keys.index(q))
                except ValueError:
                    expected.append(-1)
            #print(f"k:{keys}\nq:{queries}\ne:{expected}")
            for i, q in enumerate(queries):
                self.assertEqual(binary_search(keys, q), expected[i])
        for data in test_data:
            #print(data)
            for i, q in enumerate(data["queries"]):
                #print(i,q)
                self.assertEqual(binary_search(data["keys"], q), data["expected"][i], f"{data['keys']} {q}")

    def test_binary_search_duplicates(self):
        test_data = [
            {
                "keys":[1,5,8,8,8,8,12,13],
                "queries":[8,1,23,1,11],
                "expected": [2,0,-1,0,-1]
            },
            {
                "keys":[1,1,1,1,1],
                "queries":[1],
                "expected": [0]
            },
            {
                "keys":[1,1,1,1,1],
                "queries":[8],
                "expected": [-1]
            },
            {
                "keys":[1,1,1,10000,10000, 10000, int(10e9), int(10e9)],
                "queries":[1,10000,125,646532,int(10e9)],
                "expected": [0,3,-1,-1,6]
            },
            {
                "keys":[2,4,4,4,7,7,9],
                "queries":[9,4,5,2],
                "expected": [6,1,-1,0]
            },
        ]
        self.assertEqual(binary_search_duplicates(test_data[0]["keys"], test_data[0]["queries"][2]),  test_data[0]["expected"][2])
        for data in test_data:
            #print(data)
            for i, q in enumerate(data["queries"]):
                #print(i,q)
                self.assertEqual(binary_search_duplicates(data["keys"], q), data["expected"][i])

    def test_majority_element(self):
        self.assertEqual(majority_element([2,3,9,2,2]), 1)
        self.assertEqual(majority_element([1,2,3,4,5,6,7,8,9,10]), 0)
        self.assertEqual(majority_element([1,2,3,1]), 0)
        self.assertEqual(majority_element([1]), 0)
        self.assertEqual(majority_element([1,1,1,1,1,1,1,1,1]), 1)

        for _ in range(10):
            array_length = random.randint(1,int(10e5))
            repeated = random.randint(0, int(10e9))
            elements = [repeated for _ in range((array_length // 2) + 1)]
            elements.extend([random.randint(1, int(10e9)) for _ in range((array_length - len(elements)))])
            #print(array_length, "\t", len(elements))
            self.assertTrue(array_length == len(elements))
            self.assertEqual(majority_element(elements), 1)
        for _ in range(10):
            array_length = random.randint(1,int(10e5))
            elements = [random.randint(1,int(10e9)) for _ in range(array_length)]
            elements[-1] = 0
            #print(array_length, "\t", len(elements))
            self.assertTrue(array_length == len(elements))
            self.assertEqual(majority_element(elements), 0)
    
    def test_randomized_quick_sort(self):
        data = [
            [13, 9, 20, 17, 18, 1, 18, 13, 10, 12, 9, 14, 7, 15, 8, 16, 4, 8, 12, 17, 3, 13, 2, 3, 15, 11, 2, 8, 12, 6],
            [6, 14, 11, 12, 13, 7, 16, 15, 7, 16, 10, 17, 1, 7, 3, 6, 19, 12, 3, 14, 12, 13, 17, 9, 16, 10, 12, 18, 14, 20],
            [7, 8, 12, 15, 8, 19, 11, 20, 3, 14, 8, 2, 20, 15, 8, 7, 15, 10, 20, 10, 1, 19, 7, 18, 9, 5, 6, 8, 17, 15],
            [9, 19, 17, 5, 8, 9, 17, 4, 7, 1, 6, 10, 18, 12, 15, 10, 10, 16, 2, 5, 16, 13, 6, 8, 14, 18, 15, 16, 3, 4],
            [11, 11, 10, 4, 19, 2, 3, 7, 1, 10, 11, 10, 19, 7, 13, 7, 2, 7, 11, 2, 3, 9, 13, 12, 10, 7, 2, 8, 18, 5],
            [16, 7, 12, 10, 14, 19, 13, 13, 7, 20, 2, 5, 2, 6, 10, 3, 4, 16, 9, 8, 18, 8, 16, 17, 13, 5, 8, 6, 16, 14],
            [7, 1, 4, 11, 1, 15, 19, 17, 15, 15, 12, 15, 12, 20, 6, 8, 10, 4, 5, 19, 7, 6, 11, 1, 2, 2, 10, 16, 1, 5],
            [12, 10, 7, 17, 6, 7, 7, 1, 16, 13, 2, 1, 11, 9, 20, 10, 3, 12, 11, 17, 14, 14, 14, 10, 4, 2, 20, 6, 6, 16],
            [4, 9, 1, 12, 18, 4, 14, 8, 2, 8, 7, 7, 20, 7, 13, 9, 4, 4, 20, 18, 11, 20, 4, 14, 2, 4, 8, 6, 18, 16],
            [14, 14, 4, 9, 12, 1, 18, 7, 18, 7, 12, 13, 20, 19, 19, 10, 8, 19, 4, 16, 11, 18, 7, 15, 17, 17, 18, 16, 12, 18],
            [16, 18, 15, 9, 12, 4, 6, 3, 1, 3, 2, 3, 7, 3, 1, 11, 2, 1, 17, 5, 11, 2, 3, 15, 3, 14, 19, 16, 20, 19],
            [4, 19, 4, 19, 16, 16, 18, 19, 18, 1, 1, 2, 6, 17, 8, 15, 20, 4, 2, 8, 9, 18, 14, 19, 19, 8, 18, 20, 15, 9],
            [1, 20, 14, 1, 19, 17, 6, 19, 7, 13, 2, 5, 4, 14, 5, 7, 18, 17, 14, 13, 5, 8, 9, 4, 8, 16, 13, 6, 1, 1],
            [5, 4, 12, 9, 11, 15, 18, 17, 13, 9, 2, 6, 12, 12, 16, 18, 18, 20, 4, 15, 7, 9, 10, 20, 11, 3, 9, 15, 15, 17],
            [13, 15, 16, 10, 19, 12, 8, 7, 13, 7, 13, 12, 17, 12, 2, 15, 4, 9, 4, 15, 4, 16, 1, 11, 9, 7, 5, 1, 11, 17],
            [5, 11, 5, 14, 13, 16, 7, 6, 14, 7, 3, 4, 6, 7, 3, 11, 1, 2, 16, 6, 5, 16, 13, 6, 10, 6, 17, 6, 8, 2],
            [20, 6, 5, 10, 10, 14, 20, 13, 5, 4, 13, 7, 2, 2, 2, 6, 16, 14, 1, 10, 6, 1, 15, 17, 3, 17, 1, 12, 11, 9],
            [15, 10, 20, 6, 20, 9, 11, 17, 4, 14, 1, 15, 16, 19, 7, 15, 1, 12, 11, 16, 5, 12, 6, 20, 12, 11, 10, 18, 20, 2],
            [6, 4, 20, 19, 20, 2, 20, 19, 16, 9, 19, 18, 17, 11, 15, 1, 12, 16, 1, 14, 11, 15, 9, 7, 8, 5, 14, 15, 15, 8],
            [17, 14, 9, 6, 17, 3, 10, 17, 15, 6, 1, 12, 11, 15, 3, 19, 12, 6, 5, 15, 9, 1, 18, 19, 17, 20, 12, 20, 10, 1],
            [12, 10, 10, 6, 17, 8, 9, 1, 13, 20, 3, 16, 20, 10, 18, 4, 4, 2, 4, 3, 6, 16, 17, 12, 6, 4, 18, 19, 10, 8],
            [5, 9, 18, 9, 8, 4, 17, 16, 10, 19, 13, 18, 9, 16, 18, 1, 17, 17, 9, 16, 2, 8, 11, 12, 9, 14, 6, 9, 10, 2],
            [14, 11, 8, 12, 14, 4, 7, 13, 19, 2, 9, 12, 6, 11, 9, 16, 6, 15, 16, 19, 2, 1, 7, 20, 20, 19, 15, 8, 11, 8],
            [20, 12, 5, 19, 7, 3, 8, 18, 19, 11, 9, 12, 17, 18, 17, 6, 18, 20, 9, 14, 18, 4, 10, 6, 14, 7, 6, 1, 10, 9],
            [18, 19, 11, 1, 12, 14, 18, 13, 17, 8, 2, 13, 7, 8, 11, 20, 15, 11, 9, 18, 14, 15, 18, 4, 12, 17, 3, 1, 1, 17],
            [5, 19, 4, 19, 17, 19, 18, 8, 10, 20, 5, 14, 17, 13, 13, 15, 8, 1, 9, 15, 15, 16, 8, 1, 7, 7, 17, 18, 11, 2],
            [7, 1, 2, 11, 2, 17, 8, 9, 11, 7, 18, 8, 13, 5, 16, 18, 6, 12, 7, 1, 4, 4, 17, 5, 19, 16, 11, 10, 5, 14],
            [13, 17, 12, 1, 6, 7, 7, 20, 16, 15, 13, 13, 8, 2, 7, 18, 6, 18, 8, 19, 19, 7, 4, 8, 6, 4, 20, 1, 3, 8],
            [11, 4, 10, 10, 5, 17, 4, 14, 1, 9, 8, 6, 1, 18, 9, 8, 9, 11, 18, 13, 11, 15, 6, 13, 15, 16, 14, 12, 6, 7],
            [13, 14, 18, 13, 1, 5, 11, 4, 18, 2, 13, 18, 19, 17, 17, 19, 8, 18, 6, 2, 10, 11, 10, 20, 14, 3, 15, 10, 10, 1],
            [13, 19, 4, 4, 19, 1, 12, 13, 15, 14, 15, 2, 9, 17, 15, 19, 9, 9, 17, 6, 17, 1, 14, 14, 10, 19, 1, 18, 19, 10],
            [8, 18, 19, 12, 6, 2, 16, 4, 8, 3, 8, 20, 7, 12, 11, 6, 17, 17, 7, 8, 19, 17, 10, 5, 6, 13, 6, 15, 15, 11],
            [6, 3, 11, 16, 15, 9, 6, 15, 14, 15, 12, 3, 14, 16, 4, 19, 12, 6, 11, 10, 7, 11, 5, 19, 3, 5, 9, 9, 8, 5],
            [8, 2, 7, 16, 13, 10, 7, 1, 1, 1, 17, 7, 7, 17, 20, 4, 3, 7, 17, 20, 14, 1, 5, 9, 13, 13, 13, 11, 17, 20],
            [2, 15, 9, 3, 9, 20, 19, 19, 8, 9, 20, 14, 7, 16, 20, 8, 12, 18, 8, 6, 6, 9, 2, 5, 11, 14, 11, 3, 3, 7],
            [10, 2, 15, 20, 12, 14, 14, 14, 20, 2, 11, 17, 3, 16, 20, 16, 18, 13, 1, 19, 4, 20, 16, 4, 20, 5, 16, 18, 8, 7],
            [1, 10, 3, 19, 6, 19, 18, 10, 7, 6, 15, 12, 20, 6, 19, 16, 7, 15, 12, 13, 2, 3, 1, 4, 20, 5, 15, 19, 13, 11],
            [11, 15, 3, 7, 16, 18, 18, 1, 13, 9, 18, 9, 3, 1, 1, 14, 9, 2, 7, 15, 15, 19, 6, 2, 8, 5, 8, 12, 14, 9],
            [17, 11, 18, 17, 14, 1, 15, 5, 18, 6, 11, 7, 18, 20, 3, 15, 13, 5, 6, 1, 11, 3, 15, 5, 17, 20, 7, 20, 1, 10],
            [8, 18, 9, 3, 19, 16, 15, 1, 1, 12, 8, 17, 7, 6, 6, 3, 13, 9, 14, 16, 15, 14, 11, 1, 5, 19, 10, 3, 12, 18],
            [17, 3, 19, 16, 18, 16, 4, 3, 20, 5, 13, 18, 7, 16, 11, 7, 20, 13, 17, 13, 13, 9, 13, 16, 13, 11, 2, 15, 15, 10],
            [11, 2, 6, 5, 13, 18, 13, 2, 10, 9, 13, 13, 14, 16, 20, 18, 2, 14, 9, 12, 6, 20, 18, 3, 13, 16, 1, 9, 9, 9],
            [11, 2, 5, 18, 19, 8, 14, 18, 3, 2, 5, 4, 5, 17, 16, 8, 15, 19, 7, 11, 9, 14, 16, 4, 16, 8, 6, 18, 11, 15],
            [8, 11, 12, 12, 9, 14, 18, 1, 8, 15, 2, 6, 4, 2, 16, 4, 8, 5, 20, 12, 14, 3, 12, 8, 5, 8, 3, 4, 6, 1],
            [9, 18, 2, 1, 1, 4, 13, 20, 3, 10, 9, 3, 2, 2, 6, 10, 9, 6, 20, 15, 20, 13, 2, 1, 11, 3, 4, 14, 15, 5],
            [4, 19, 5, 4, 14, 16, 10, 11, 8, 1, 1, 19, 20, 5, 7, 20, 14, 14, 18, 11, 15, 19, 13, 7, 11, 10, 19, 14, 9, 6],
            [8, 6, 15, 14, 10, 11, 13, 13, 5, 18, 1, 18, 10, 8, 13, 6, 6, 11, 8, 18, 14, 7, 8, 11, 11, 14, 2, 5, 8, 4],
            [10, 19, 1, 6, 11, 9, 17, 1, 8, 1, 11, 18, 8, 19, 4, 20, 16, 9, 20, 2, 20, 20, 20, 11, 1, 7, 8, 8, 16, 1],
            [14, 11, 11, 11, 20, 7, 7, 11, 8, 1, 9, 16, 11, 6, 8, 15, 7, 14, 6, 3, 14, 18, 13, 17, 6, 8, 11, 3, 13, 11],
            [9, 19, 2, 14, 10, 12, 4, 17, 14, 18, 20, 14, 3, 12, 15, 13, 19, 11, 16, 1, 14, 18, 17, 13, 1, 5, 2, 20, 20, 9],
            [7, 2, 11, 13, 18, 4, 14, 1, 18, 12, 19, 12, 15, 4, 16, 11, 12, 15, 20, 3, 9, 13, 8, 7, 8, 11, 15, 16, 13, 20],
            [2, 18, 3, 13, 3, 7, 9, 19, 18, 11, 3, 15, 16, 12, 6, 17, 7, 15, 20, 19, 1, 2, 3, 9, 12, 9, 2, 5, 12, 4],
            [3, 9, 10, 6, 11, 15, 14, 11, 1, 17, 4, 11, 1, 19, 3, 1, 2, 6, 12, 1, 2, 8, 18, 16, 5, 16, 19, 8, 5, 10],
            [2, 12, 7, 18, 18, 20, 15, 1, 13, 16, 8, 5, 4, 7, 6, 11, 19, 4, 9, 14, 5, 16, 13, 19, 12, 5, 10, 18, 18, 4],
            [11, 3, 14, 6, 15, 13, 9, 2, 17, 13, 19, 6, 1, 12, 11, 18, 5, 13, 19, 16, 20, 1, 14, 4, 19, 13, 9, 6, 6, 16],
            [3, 9, 5, 20, 1, 17, 6, 4, 13, 1, 6, 11, 4, 6, 19, 4, 16, 3, 15, 8, 17, 11, 3, 8, 9, 16, 9, 5, 5, 12],
            [17, 12, 2, 3, 9, 9, 11, 5, 14, 5, 16, 8, 8, 10, 16, 9, 14, 11, 1, 16, 1, 15, 3, 6, 4, 17, 18, 11, 14, 19],
            [1, 7, 9, 20, 11, 5, 4, 8, 2, 19, 13, 17, 5, 2, 11, 8, 15, 7, 3, 20, 16, 12, 5, 10, 3, 19, 11, 3, 8, 16],
            [14, 13, 18, 11, 5, 18, 20, 5, 9, 5, 3, 4, 7, 1, 16, 20, 7, 16, 7, 4, 7, 7, 17, 9, 10, 13, 10, 17, 14, 19],
            [4, 4, 2, 3, 4, 12, 6, 15, 18, 18, 15, 9, 6, 9, 14, 18, 9, 6, 3, 16, 12, 3, 11, 14, 8, 15, 18, 13, 10, 17],
            [5, 13, 5, 9, 15, 13, 8, 4, 18, 18, 13, 6, 4, 7, 11, 18, 18, 14, 16, 7, 4, 6, 6, 17, 11, 19, 8, 12, 5, 12],
            [4, 6, 10, 16, 14, 19, 15, 2, 3, 20, 1, 16, 1, 18, 17, 2, 7, 1, 15, 4, 8, 14, 10, 16, 20, 4, 13, 17, 20, 20],
            [13, 14, 6, 17, 11, 20, 20, 19, 1, 19, 5, 5, 15, 3, 15, 14, 9, 16, 11, 18, 3, 15, 4, 10, 6, 17, 3, 6, 12, 20],
            [4, 18, 12, 12, 10, 18, 10, 8, 7, 3, 16, 11, 4, 18, 14, 15, 9, 6, 14, 5, 9, 4, 12, 4, 15, 8, 18, 17, 18, 12],
            [1, 6, 1, 7, 8, 1, 12, 17, 16, 6, 14, 5, 13, 19, 5, 5, 14, 7, 12, 20, 3, 5, 15, 9, 11, 16, 16, 8, 7, 7],
            [17, 8, 16, 5, 14, 11, 12, 8, 9, 2, 18, 8, 11, 9, 18, 8, 14, 3, 19, 6, 15, 12, 4, 13, 19, 1, 8, 7, 5, 4],
            [18, 1, 17, 20, 4, 7, 16, 15, 5, 16, 3, 14, 14, 5, 10, 18, 5, 10, 14, 5, 13, 19, 8, 5, 12, 20, 20, 11, 17, 10],
            [5, 18, 11, 15, 9, 6, 10, 15, 5, 3, 2, 15, 10, 9, 20, 13, 7, 15, 7, 9, 5, 20, 16, 17, 3, 5, 16, 18, 6, 10],
            [6, 8, 14, 5, 11, 8, 15, 5, 17, 4, 11, 14, 17, 4, 4, 4, 14, 17, 14, 10, 3, 15, 14, 4, 2, 13, 9, 6, 10, 19],
            [20, 3, 1, 15, 19, 15, 6, 10, 11, 6, 3, 11, 19, 11, 20, 12, 19, 10, 16, 13, 6, 9, 8, 1, 15, 16, 2, 6, 14, 18],
            [2, 2, 7, 18, 17, 20, 13, 2, 10, 14, 11, 1, 13, 4, 2, 15, 8, 19, 13, 13, 11, 9, 4, 19, 10, 14, 1, 14, 17, 1],
            [12, 13, 19, 16, 15, 1, 14, 16, 18, 3, 14, 2, 13, 20, 14, 18, 19, 5, 13, 4, 6, 11, 20, 5, 8, 12, 20, 1, 13, 3],
            [3, 7, 11, 16, 13, 5, 15, 2, 7, 14, 19, 10, 14, 12, 16, 4, 1, 7, 8, 2, 19, 19, 11, 18, 20, 17, 7, 13, 13, 3],
            [19, 19, 8, 4, 17, 1, 14, 15, 19, 10, 10, 1, 13, 6, 11, 11, 3, 12, 9, 6, 15, 3, 16, 12, 17, 6, 11, 20, 3, 15],
            [14, 13, 14, 12, 12, 9, 15, 19, 10, 1, 9, 16, 4, 10, 14, 7, 7, 1, 10, 15, 13, 9, 19, 19, 3, 18, 6, 19, 17, 8],
            [13, 19, 12, 19, 8, 9, 15, 10, 10, 19, 16, 15, 5, 3, 1, 15, 15, 4, 11, 8, 6, 19, 20, 12, 4, 5, 6, 15, 13, 13],
            [19, 17, 11, 17, 12, 9, 10, 17, 14, 8, 4, 9, 14, 5, 17, 15, 20, 3, 15, 11, 16, 2, 7, 16, 15, 10, 1, 15, 8, 2],
            [2, 18, 7, 13, 11, 8, 18, 16, 15, 14, 9, 2, 3, 1, 17, 5, 16, 3, 3, 7, 1, 1, 1, 12, 6, 7, 2, 11, 13, 4],
            [13, 20, 6, 3, 17, 16, 9, 8, 16, 9, 1, 3, 15, 10, 9, 3, 9, 16, 15, 4, 19, 13, 11, 14, 19, 10, 19, 13, 10, 5],
            [8, 8, 18, 1, 7, 13, 15, 10, 14, 5, 1, 16, 13, 3, 6, 7, 3, 13, 19, 3, 11, 6, 17, 17, 10, 11, 2, 8, 3, 11],
            [17, 1, 12, 8, 17, 9, 6, 2, 9, 11, 20, 10, 19, 16, 15, 16, 14, 4, 11, 5, 13, 19, 11, 3, 1, 14, 3, 4, 4, 15],
            [15, 1, 1, 5, 19, 15, 1, 4, 2, 13, 4, 5, 14, 4, 20, 18, 10, 20, 3, 1, 12, 7, 1, 8, 8, 8, 15, 7, 3, 6],
            [9, 8, 3, 1, 4, 15, 1, 3, 5, 2, 17, 12, 16, 5, 7, 13, 5, 17, 6, 2, 1, 6, 3, 14, 17, 11, 3, 20, 15, 18],
            [8, 16, 1, 2, 20, 13, 15, 7, 18, 11, 9, 10, 15, 4, 19, 13, 4, 6, 4, 11, 18, 10, 13, 17, 9, 1, 8, 3, 18, 2],
            [15, 16, 7, 8, 2, 3, 20, 14, 10, 19, 16, 1, 2, 20, 10, 1, 19, 20, 2, 10, 20, 15, 10, 14, 7, 11, 15, 20, 2, 13],
            [2, 16, 15, 11, 3, 12, 15, 12, 18, 11, 13, 15, 7, 2, 4, 1, 10, 5, 14, 7, 14, 20, 13, 15, 4, 6, 2, 3, 20, 4],
            [5, 7, 6, 11, 5, 12, 14, 10, 20, 20, 8, 3, 2, 6, 3, 13, 8, 9, 11, 16, 10, 15, 9, 2, 2, 18, 19, 16, 18, 13],
            [9, 10, 19, 17, 20, 13, 11, 20, 16, 3, 19, 7, 15, 16, 20, 18, 17, 15, 7, 17, 2, 19, 18, 12, 7, 19, 17, 11, 7, 20],
            [16, 19, 13, 5, 20, 10, 9, 1, 18, 18, 19, 6, 20, 10, 10, 6, 16, 6, 5, 15, 2, 20, 12, 4, 15, 15, 3, 18, 7, 5],
            [11, 2, 5, 20, 13, 14, 12, 13, 2, 15, 20, 11, 19, 15, 4, 13, 16, 5, 18, 3, 13, 19, 16, 3, 6, 12, 18, 7, 9, 17],
            [12, 7, 11, 8, 7, 19, 15, 6, 19, 11, 1, 5, 12, 6, 10, 16, 10, 6, 19, 14, 11, 15, 2, 19, 2, 1, 16, 15, 20, 14],
            [20, 5, 13, 11, 20, 17, 5, 2, 9, 18, 15, 10, 16, 10, 4, 2, 14, 3, 10, 7, 12, 9, 18, 20, 9, 13, 16, 15, 19, 17],
            [1, 15, 16, 1, 15, 14, 18, 19, 19, 19, 7, 1, 8, 15, 8, 14, 11, 13, 19, 15, 6, 9, 11, 15, 14, 8, 15, 9, 5, 6],
            [6, 9, 6, 9, 8, 15, 14, 13, 6, 4, 15, 15, 8, 4, 6, 9, 14, 17, 2, 7, 17, 19, 6, 1, 13, 18, 19, 8, 5, 2],
            [13, 6, 18, 1, 3, 5, 10, 14, 16, 18, 19, 13, 8, 6, 2, 8, 11, 7, 13, 2, 9, 15, 4, 18, 9, 4, 10, 1, 15, 11],
            [6, 12, 4, 6, 5, 11, 7, 9, 15, 11, 17, 17, 5, 1, 5, 7, 18, 18, 8, 19, 18, 6, 6, 2, 11, 12, 4, 3, 10, 9],
            [1, 13, 19, 13, 12, 19, 16, 6, 1, 6, 11, 2, 5, 5, 9, 3, 9, 7, 1, 3, 15, 2, 2, 20, 17, 3, 6, 20, 11, 19],
            [17, 8, 16, 5, 16, 20, 15, 11, 10, 4, 7, 8, 10, 17, 15, 18, 17, 18, 4, 1, 13, 19, 7, 16, 16, 9, 1, 2, 5, 8],
            [12, 6, 5, 11, 10, 7, 19, 16, 16, 20, 12, 9, 9, 14, 6, 12, 9, 4, 2, 2, 17, 13, 19, 19, 7, 13, 4, 6, 6, 7],
            [20, 5, 5, 10, 1, 2, 16, 2, 4, 1, 2, 11, 8, 4, 6, 15, 18, 2, 2, 1, 10, 6, 6, 20, 12, 5, 1, 1, 11, 20],

        ]
        def generate():
            with open("unsorted_elements.txt", mode="w") as file:
                for _ in range (100):
                    file.write(str([random.randint(1,20) for _ in range(30)]))
                    file.write(",\n")
        for i in range(30):
            array = data[i]
            left = 0
            right = len(array) - 1
            expected = sorted(data[i])
            self.assertEqual(randomized_quick_sort(array, left, right), expected)

        for _ in range(100):
            data = [random.randint(1, int(10e9)) for _ in range(random.randint(1,int(10e5)))]

    def test_inversion(self):
        MAX_LENGTH = 30_000
        MAX_VALUE = int(10e9)

        for _ in range(1000):
            length = random.randint(1,100)
            value = random.randint(1, 1000)
            data = [random.randint(1,value) for _ in range(length)]
            #print("\n",data)
            expected = inversions_naive(data)
            print(f"expected: {expected}")
            actual = inversions(data)
            print(f"actual: {actual}")
            self.assertEqual(actual, expected)
        
        for _ in range(10):
            length = random.randint(1,MAX_LENGTH)
            value = random.randint(1, MAX_LENGTH)
            data = [random.randint(1,value) for _ in range(length)]
            actual = inversions(data)
            print(f"actual: {actual}")
'''
    def test_points_cover(self):
        MAX_POINTS = 50000
        MAX_SEGMENTS = 50000
        MIN_VALUE = -int(10e8)
        MAX_VALUE = int(10e8)
        
        self.assertEqual(points_cover([0,7],[5,10],[1,6,11]),[1,0,0])
        self.assertEqual(points_cover([-10],[10],[-100,100,0]),[0,0,1])
        self.assertEqual(points_cover([0,-3,7],[5,2,10],[1,6]),[2,0])
        
        for _ in range(100):
            starts, ends, points = [],[],[]
            samples = 500
            num_segments = random.randint(1, samples)
            num_points = random.randint(1, samples)
            minimum = random.randint(-100,0)
            maximum = random.randint(0,100)
            
            for _ in range(num_segments):
                num1, num2 = random.randint(minimum, maximum), random.randint(minimum, maximum)
                start = starts.append(min(num1, num2))
                end = ends.append(max(num1, num2))

            for _ in range(num_points):
                points.append(random.randint(minimum, maximum))

            self.assertEqual(points_cover_naive(starts, ends, points), points_cover(starts, ends, points))
        print("Naive and Fast produce same result")

        for _ in range(1):
            starts, ends, points = [],[],[]
            samples = MAX_POINTS
            num_segments = random.randint(1, samples)
            num_points = random.randint(1, samples)
            first = random.randint(MIN_VALUE, MAX_VALUE)
            second = random.randint(MIN_VALUE, MAX_VALUE)
            minimum = min(first, second)
            maximum = max(first, second)
            
            for _ in range(num_segments):
                num1, num2 = random.randint(minimum, maximum), random.randint(minimum, maximum)
                starts.append(min(num1, num2))
                ends.append(max(num1, num2))

            for _ in range(num_points):
                points.append(random.randint(minimum, maximum))
            
            points_cover(starts, ends, points)

    def test_minimum_square_dstance(self):
        from collections import namedtuple
        Point = namedtuple('Point', 'x y')
        MIN_LENGTH = 2
        MAX_LENGTH = int(10e5)
        MIN_VALUE = -int(10e9)
        MAX_VALUE = int(10e9)

        data = [
            [
                Point(0,0), Point(3,4)
            ],
            [
                Point(4,4), Point(-2,-2), Point(-3,-4),
                Point(-1,3), Point(2,3), Point(-4,0), Point(1,1),
                Point(-1,-1), Point(3,-1), Point(-4,2), Point(-2,4)
            ],
            
        ]

        self.assertAlmostEqual(minimum_distance_squared_naive(data[0]), 5.0**2 ,3)
        self.assertAlmostEqual(minimum_distance_squared_naive(data[1]), 1.414213**2 ,3)

        self.assertAlmostEqual(minimum_distance_squared_naive(data[0]),
                               mds(data[0]),
                               3)
        self.assertAlmostEqual(minimum_distance_squared_naive(data[1]),
                               mds(data[1]),
                               3)
    
        for _ in range(1):
            length = random.randint(MIN_LENGTH, MAX_LENGTH) // 1000
            value = abs(random.randint(MIN_VALUE, MAX_VALUE)) // 1_000_000
            points = []
            for _ in range(length):
                num1, num2 = random.randint(-value, value), random.randint(-value, value)
                low, high  = min(num1, num2), max(num1, num2)
                points.append(Point(
                        random.randint(low, high),
                        random.randint(low, high)                        
                        )
                    )
            print(mds(points))
            self.assertAlmostEqual(minimum_distance_squared_naive(points), mds(points), 3)
'''
if __name__ == "__main__":
    unittest.main()