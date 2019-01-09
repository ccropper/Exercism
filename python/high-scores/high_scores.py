"""
Your task is to write methods that return the highest score from the
list, the last added score, the three highest scores, and a report
on the difference between the last and the highest scores.
"""

class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top(self):
        return sorted(self.scores, reverse=True)[:3]

    def report(self):
        if self.latest() == self.personal_best():
            return "Your latest score was %s. That's your personal best!" % (self.latest())
        else:
            return "Your latest score was %s. That's %s short of your personal best!" % (self.latest(), self.personal_best() - self.latest())
