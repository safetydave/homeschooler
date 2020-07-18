

class Tasks:

    TASKS_2_YES = {'A': 5, 'B': 1, 'C': 4}
    TASKS_3_YES = {'A': 5, 'B': 4, 'C': 1, 'D': 2, 'E': 7, 'F': 8, 'G': 3}
    TASKS_4_YES = {'A': 2, 'B': 5, 'C': 1, 'D': 6, 'E': 4, 'F': 2, 'G': 1, 'H': 3, 'I': 2, 'J': 2}
    TASKS_3_NUP = {'A': 5, 'B': 4, 'C': 1, 'D': 2, 'E': 7, 'F': 12, 'G': 2}

    def __init__(self, t):
        self.t = t
        self.efforts = [t[1] for t in self.t.items()]
        self.total_effort = sum(self.efforts)
        self.keys_asc = sorted(list(self.t.keys()))
        self.t_efforts_desc = [(k, v) for k, v in reversed(sorted(self.t.items(), key=lambda x: x[1]))]

    def can_count_split(self, n):
        return len(self.t) >= n

    def can_total_split(self, n):
        return self.total_effort % n == 0

    def target_effort(self, n):
        return self.total_effort // n

    def has_oversize_tasks(self, n):
        return max(self.efforts) > self.target_effort(n)

