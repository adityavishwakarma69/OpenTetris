from srcs.timer import *

class Diff:
    def __init__(self, diffs, diffstep):
        self.diffs = diffs
        self.diffstep = diffstep
        self.currdiff = 0
        self.timer = Timer(diffs[self.currdiff])

    def update(self, game, dt):
        if game.score > (self.diffstep * (self.currdiff + 1)):
            if self.currdiff < (len(self.diffs) - 1):
                self.currdiff += 1
                self.timer.new(self.diffs[self.currdiff])
        
        if self.timer.timeout(dt):
            game.moveDown()
            return True
        return False
