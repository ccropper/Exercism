import random
import string

class Robot(object):
    def __init__(self):
        self.name = self.generate_name()
    
    def generate_name(self):
        return ''.join(random.choices(string.ascii_uppercase, k=2)) + ''.join(random.choices(string.digits, k=3))

    def reset(self):
        self.name = self.generate_name()