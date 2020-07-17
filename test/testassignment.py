import unittest

from homeschooler.assignment import Assignment, assign_round_robin_oscillating
from homeschooler.tasks import Tasks


class TestAssignment(unittest.TestCase):

    def setUp(self):
        self.a = (0, 0, 1)

    def test_neighbours(self):
        assignment = Assignment(self.a)
        neighbours = assignment.neighbours(2)
        self.assertEqual(neighbours[0], (1, 0, 1))
        self.assertEqual(neighbours[1], (0, 1, 1))
        self.assertEqual(neighbours[2], (0, 0, 0))

    def test_assign_round_robin_oscillating(self):
        a = assign_round_robin_oscillating(Tasks(Tasks.TASKS_2_YES), 2)
        self.assertEqual(a, (0, 1, 1))