import unittest

from homeschooler.tasks import Tasks


class TestTasks(unittest.TestCase):

    def setUp(self):
        self.t2y = Tasks(Tasks.TASKS_2_YES)
        self.t3y = Tasks(Tasks.TASKS_3_YES)
        self.t4y = Tasks(Tasks.TASKS_4_YES)
        self.t3n = Tasks(Tasks.TASKS_3_NUP)

    def test_can_count_split(self):
        self.assertTrue(self.t2y.can_count_split(2))
        self.assertFalse(self.t2y.can_count_split(4))

    def test_can_total_split(self):
        self.assertTrue(self.t3y.can_total_split(3))
        self.assertFalse(self.t3y.can_total_split(4))

    def test_target_effort(self):
        self.assertEqual(self.t3y.target_effort(3), 10)
        self.assertEqual(self.t4y.target_effort(4), 7)

    def test_has_oversize_tasks(self):
        self.assertTrue(self.t3n.has_oversize_tasks(3))
        self.assertFalse(self.t3y.has_oversize_tasks(3))


if __name__ == '__main__':
    unittest.main()
