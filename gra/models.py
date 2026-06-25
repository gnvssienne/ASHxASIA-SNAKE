from constants import COLS, ROWS

class Snake:
    def __init__(self):
        self.body = [PVector(COLS // 2, ROWS // 2)]
        self.xdir = 1
        self.ydir = 0
        self.grow_pending = False

    def update(self):
        
        head = self.body[0].copy()
        head.x += self.xdir
        head.y += self.ydir
        self.body.insert(0, head)
        
        if not self.grow_pending:
            self.body.pop()
        else:
            self.grow_pending = False

    def grow(self):
        self.grow_pending = True

    def set_dir(self, x, y):
        if self.xdir != -x or self.ydir != -y:
            self.xdir = x
            self.ydir = y

#Asia collisions
    def check_collision(self, obstacles):
        head = self.body[0]
        # Wall collision
        if head.x < 0 or head.x >= COLS or head.y < 0 or head.y >= ROWS:
            return True
        # Self collision
        for part in self.body[1:]:
            if head.x == part.x and head.y == part.y:
                return True
        # Obstacle collision
        for obs in obstacles:
            if head.x == obs.x and head.y == obs.y:
                return True
        return False

class Food:
    def __init__(self):
        self.pos = self.pick_location()

    def pick_location(self):
        return PVector(int(random(COLS)), int(random(ROWS)))
