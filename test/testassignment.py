import unittest

from homeschooler.assignment import Assignment


class TestTasks(unittest.TestCase):

    def setUp(self):
        self.a = (0, 0, 1)

    def testneighbours(self):
        assignment = Assignment(self.a)
        neighbours = assignment.neighbours(2)
        self.assertTrue(neighbours[0], (1, 0, 1))
        self.assertTrue(neighbours[1], (0, 1, 1))
        self.assertTrue(neighbours[2], (0, 0, 0))