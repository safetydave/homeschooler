import unittest

from homeschooler.assignment import assign_rro, neighbours
from homeschooler.tasks import Tasks


class TestAssignment(unittest.TestCase):

    def setUp(self):
        self.a = (0, 0, 1)

    def test_neighbours(self):
        ns = neighbours(self.a, 2)
        self.assertEqual(ns[0], (1, 0, 1))
        self.assertEqual(ns[1], (0, 1, 1))
        self.assertEqual(ns[2], (0, 0, 0))

    def test_assign_rro(self):
        a = assign_rro(Tasks(Tasks.TASKS_2_YES), 2)
        self.assertEqual(a, (0, 1, 1))
