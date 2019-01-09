import random
import string

class Robot(object):
    used_names = []
    
    def __init__(self):
        self.name = self.generate_unique_name()
        
    def generate_unique_name(self):
        used_name = True
        while used_name:
            new_name = ''.join(random.choices(string.ascii_uppercase, k=2)) + ''.join(random.choices(string.digits, k=3))
            if new_name not in Robot.used_names:
                used_name = False
        if used_name == False:
            Robot.used_names.append(new_name)
            return new_name

    def reset(self):
        self.name = self.generate_unique_name()