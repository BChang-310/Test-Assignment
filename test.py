import unittest
import nbconvert
import numpy as np

with open("assignment.ipynb") as f:
    exporter = nbconvert.PythonExporter()
    python_file, _ = exporter.from_file(f)

with open("assignment.py", "w") as f:
    f.write(python_file)

from assignment import *

class TestSolution(unittest.TestCase):
    def test_prob1_1(self):
        np.testing.assert_string_equal(problem_1(), "Hello, world!")

    def test_prob1_2(self):
        np.testing.assert_equal(problem_2(2, 4), 6)

    def test_prob1_3(self):
        np.testing.assert_equal(problem_3(6), 15)



if __name__ == '__main__':
    unittest.main()
