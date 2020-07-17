import unittest

from homeschooler.assignment import Assignment


class TestAssignment(unittest.TestCase):

    def setUp(self):
        self.a = (0, 0, 1)

    def test_neighbours(self):
        assignment = Assignment(self.a)
        neighbours = assignment.neighbours(2)
        self.assertEqual(neighbours[0], (1, 0, 1))
        self.assertEqual(neighbours[1], (0, 1, 1))
        self.assertEqual(neighbours[2], (0, 0, 0))
