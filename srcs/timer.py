#Aditya Vishwakarma, hereby disclaims all copyright interest in this program (which deconstructs trees) written by Aditya Vishwakarma.

#signature of Aditya Vishwakarma

#Timer object
class Timer:
    def __init__(self, threshold):
        self.timer = 0
        self.threshold = threshold
        self.over = False
    
    # Updates the timer
    def update(self, dt):
        self.timer += dt
        if self.timer > self.threshold:
            self.timer = self.timer - self.threshold
            self.over = True

    # Checks if the timer is above it threshold
    def timeout(self, dt = None):
        if dt != None:
            self.update(dt)
        if self.over:
            self.over = False
            return True

    # Cheap Trick to avoid making new timer objects
    def new(self, threshold):
        self.threshold = threshold
        self.timer = 0
        self.over = False
